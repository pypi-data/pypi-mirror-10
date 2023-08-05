"""
httping.py

nonblocking http classes


"""
#print("module {0}".format(__name__))

from __future__ import division


import sys
import os
import socket
import errno
import io
from collections import deque
import codecs
import json
import ssl

if sys.version > '3':
    from urllib.parse import urlsplit
else:
    from urlparse import urlsplit

from email.parser import HeaderParser

# Import ioflo libs
from .sixing import *
from ..base.odicting import odict, lodict
from ..base import excepting
from .nonblocking import Outgoer, OutgoerTls

from ..base.consoling import getConsole
console = getConsole()

CRLF = b"\r\n"
LF = b"\n"
CR = b"\r"
MAX_LINE_SIZE = 65536
MAX_HEADERS = 100

HTTP_PORT = 80
HTTPS_PORT = 443
HTTP_11_VERSION_STRING = u'HTTP/1.1'  # http v1.1 version string

# status codes
# informational
CONTINUE = 100

# These constants are here for potential backwards compatibility
# currently most are unused
# status codes
# informational

SWITCHING_PROTOCOLS = 101
PROCESSING = 102

# successful
OK = 200
CREATED = 201
ACCEPTED = 202
NON_AUTHORITATIVE_INFORMATION = 203
NO_CONTENT = 204
RESET_CONTENT = 205
PARTIAL_CONTENT = 206
MULTI_STATUS = 207
IM_USED = 226

# redirection
MULTIPLE_CHOICES = 300
MOVED_PERMANENTLY = 301
FOUND = 302
SEE_OTHER = 303
NOT_MODIFIED = 304
USE_PROXY = 305
TEMPORARY_REDIRECT = 307

# client error
BAD_REQUEST = 400
UNAUTHORIZED = 401
PAYMENT_REQUIRED = 402
FORBIDDEN = 403
NOT_FOUND = 404
METHOD_NOT_ALLOWED = 405
NOT_ACCEPTABLE = 406
PROXY_AUTHENTICATION_REQUIRED = 407
REQUEST_TIMEOUT = 408
CONFLICT = 409
GONE = 410
LENGTH_REQUIRED = 411
PRECONDITION_FAILED = 412
REQUEST_ENTITY_TOO_LARGE = 413
REQUEST_URI_TOO_LONG = 414
UNSUPPORTED_MEDIA_TYPE = 415
REQUESTED_RANGE_NOT_SATISFIABLE = 416
EXPECTATION_FAILED = 417
UNPROCESSABLE_ENTITY = 422
LOCKED = 423
FAILED_DEPENDENCY = 424
UPGRADE_REQUIRED = 426
PRECONDITION_REQUIRED = 428
TOO_MANY_REQUESTS = 429
REQUEST_HEADER_FIELDS_TOO_LARGE = 431

# server error
INTERNAL_SERVER_ERROR = 500
NOT_IMPLEMENTED = 501
BAD_GATEWAY = 502
SERVICE_UNAVAILABLE = 503
GATEWAY_TIMEOUT = 504
HTTP_VERSION_NOT_SUPPORTED = 505
INSUFFICIENT_STORAGE = 507
NOT_EXTENDED = 510
NETWORK_AUTHENTICATION_REQUIRED = 511

# Mapping status codes to official W3C names
responses = {
    100: 'Continue',
    101: 'Switching Protocols',

    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',

    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    306: '(Unused)',
    307: 'Temporary Redirect',

    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Request Entity Too Large',
    414: 'Request-URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',
    428: 'Precondition Required',
    429: 'Too Many Requests',
    431: 'Request Header Fields Too Large',

    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    511: 'Network Authentication Required',
}

# maximal amount of data to read at one time in _safe_read
MAXAMOUNT = 1048576

# maximal line length when calling readline().
_MAXLINE = 65536
_MAXHEADERS = 100

class HTTPException(Exception):
    # Subclasses that define an __init__ must call Exception.__init__
    # or define self.args.  Otherwise, str() will fail.
    pass

class InvalidURL(HTTPException):
    pass


class UnknownProtocol(HTTPException):
    def __init__(self, version):
        self.args = version,
        self.version = version

class BadStatusLine(HTTPException):
    def __init__(self, line):
        if not line:
            line = repr(line)
        self.args = line,
        self.line = line


class LineTooLong(HTTPException):
    def __init__(self, kind):
        HTTPException.__init__(self, "got more than %d bytes while parsing %s"
                                     % (MAX_LINE_SIZE, kind))


# these are here for potential backwards compatibility
# currently unused

class NotConnected(HTTPException):
    pass

class UnknownTransferEncoding(HTTPException):
    pass

class UnimplementedFileMode(HTTPException):
    pass

class IncompleteRead(HTTPException):
    def __init__(self, partial, expected=None):
        self.args = partial,
        self.partial = partial
        self.expected = expected
    def __repr__(self):
        if self.expected is not None:
            e = ', %i more expected' % self.expected
        else:
            e = ''
        return 'IncompleteRead(%i bytes read%s)' % (len(self.partial), e)
    def __str__(self):
        return repr(self)

class ImproperConnectionState(HTTPException):
    pass

class CannotSendRequest(ImproperConnectionState):
    pass

class CannotSendHeader(ImproperConnectionState):
    pass

class ResponseNotReady(ImproperConnectionState):
    pass

class WaitLine(HTTPException):
    def __init__(self, kind, actual, index):
        self.args = (kind, actual, index)
        self.kind = kind
        self.actual = actual
        self.index = index

    def __repr__(self):
        emsg = ("Waited parsing {0}. Line end still missing after {1} bytes "
            "past {2}".formate(self.kind, self.actual, self.index))
        return emsg

    def __str__(self):
        return repr(self)

class WaitContent(HTTPException):
    def __init__(self, actual, expected, index):
        self.args = (actual, expected, index)
        self.actual = actual
        self.expected = expected
        self.index = index

    def __repr__(self):
        emsg = ("Waited need more bytes. Line end missing after {0} bytes "
            "past {1} while parsing {2}".formate(self.count, self.index, self.kind))
        return emsg

    def __str__(self):
        return repr(self)

# Utility functions

def normalizeHostPort(host, port, defaultPort=80):
    if port is None:
        i = host.rfind(u':')
        j = host.rfind(u']')         # ipv6 addresses have [...]
        if i > j:
            try:
                port = int(host[i+1:])
            except ValueError:
                if host[i+1:] == u"": # foo.com: == foo.com
                    port = defaultPort
                else:
                    raise InvalidURL("nonnumeric port: '%s'" % host[i+1:])
            host = host[:i]
        else:
            port = defaultPort
        if host and host[0] == u'[' and host[-1] == u']':
            host = host[1:-1]
    return (host, port)

#  Non Blocking Class Definitions
class Requester(object):
    """
    Nonblocking HTTP Request class
    """
    HttpVersionString = HTTP_11_VERSION_STRING  # http version string
    Port = HTTP_PORT  # default port

    def __init__(self,
                 host='127.0.0.1',
                 port=None,
                 method=u'GET',  # unicode
                 url=u'/',  # unicode
                 headers=None,
                 body=b'',):
        """
        Initialize Instance

        host = remote server host address (may include port as host:port)
        port = remote server port
        method = http request method verb
        url = http url
        body = http request body
        """
        self.host, self.port = normalizeHostPort(host, port, 80)
        self.method = method.upper() if method else u'GET'
        self.url = url or u'/'
        self.headers = headers or odict()

        if body and isinstance(body, unicode):  # use default
            # RFC 2616 Section 3.7.1 default charset of iso-8859-1.
            body = body.encode('iso-8859-1')
        self.body = body or b''

        self.lines = []
        self.head = b""
        self.msg = b""

    def reinit(self,
               method=None,  # unicode
               url=None,  # unicode
               headers=None,
               body=None,):
        """
        Reinitialize anything that is not None
        This enables creating another request on a connection to the same host port
        """
        if method is not None:
            self.method = method.upper()
        if url is not None:
            self.url = url
        if headers is not None:
            self.headers = headers
        if body is not None:
            if isinstance(body, unicode):
                # RFC 2616 Section 3.7.1 default charset of iso-8859-1.
                body = body.encode('iso-8859-1')
            self.body = body

    def build(self, method=None, url=None, headers=None, body=None):
        """
        Build and return request message

        """
        self.reinit(method, url, headers, body)
        self.lines = []

        headerKeys = dict.fromkeys([unicode(k.lower()) for k in self.headers])

        skip_accept_encoding = True if 'accept-encoding' in headerKeys else False

        startLine = "{0} {1} {2}".format(self.method, self.url, self.HttpVersionString)
        self.lines.append(startLine.encode('ascii'))

        if u'host' not in headerKeys:
            # If we need a non-standard port, include it in the header
            netloc = ''
            if self.url.startswith('http'):
                nil, netloc, nil, nil, nil = urlsplit(url)

            if netloc:
                try:
                    netloc_enc = netloc.encode("ascii")
                except UnicodeEncodeError:
                    netloc_enc = netloc.encode("idna")
                self.lines.append(self.packHeader(u'Host', netloc_enc))
            else:
                host = self.host
                port = self.port

                try:
                    host_enc = host.encode("ascii")
                except UnicodeEncodeError:
                    host_enc = host.encode("idna")

                # As per RFC 273, IPv6 address should be wrapped with []
                # when used as Host header

                if host.find(':') >= 0:
                    host_enc = b'[' + host_enc + b']'

                if port == self.Port:
                    self.lines.append(self.packHeader('Host', host_enc))
                else:
                    host_enc = host_enc.decode("ascii")
                    self.lines.append(self.packHeader('Host', "{0}:{1}".format(host_enc, port)))

        # we only want a Content-Encoding of "identity" since we don't
        # support encodings such as x-gzip or x-deflate.
        if u'accept-encoding' not in headerKeys:
            self.lines.append(self.packHeader('Accept-Encoding', 'identity'))

        if self.body is not None and (u'content-length' not in headerKeys):
            self.lines.append(self.packHeader('Content-Length', str(len(self.body))))

        for name, value in self.headers.items():
            self.lines.append(self.packHeader(name, value))

        self.lines.extend((b"", b""))
        self.head = CRLF.join(self.lines)  # b'/r/n'

        self.msg = self.head + self.body
        return self.msg

    def packHeader(self, name, *values):
        """
        Format and return a request header line.

        For example: h.packHeader('Accept', 'text/html')
        """
        if isinstance(name, unicode):  # not bytes
            name = name.encode('ascii')
        name = name.title()
        values = list(values)  # make copy
        for i, value in enumerate(values):
            if isinstance(value, unicode):
                values[i] = value.encode('iso-8859-1')
            elif isinstance(value, int):
                values[i] = str(value).encode('ascii')
        value = b', '.join(values)
        value = value.lower()
        return (name + b': ' + value)


def parseLine(raw, eols=(CRLF, LF, CR ), kind="event line"):
    """
    Generator to parse  line from raw bytearray
    Each line demarcated by one of eols
    kind is line type string for error message

    Yields None If waiting for more to parse
    Yields line Otherwise

    Consumes parsed portions of raw bytearray

    Raise error if eol not found before MAX_LINE_SIZE
    """
    while True:
        for eol in eols:  # loop over eols unless found
            index = raw.find(eol)  # not found index == -1
            if index >= 0:
                break

        if index < 0:  # not found
            if len(raw) > MAX_LINE_SIZE:
                raise LineTooLong(kind)
            else:
                (yield None)  # more data needed not done parsing header
                continue

        if index > MAX_LINE_SIZE:  # found but line too long
            raise LineTooLong(kind)

        line = raw[:index]
        index += len(eol)  # strip eol
        del raw[:index] # remove used bytes
        (yield line)
    return

def parseBom(raw, bom=codecs.BOM_UTF8):
    """
    Generator to parse bom from raw bytearray
    Yields None If waiting for more to parse
    Yields bom If found
    Yields empty bytearray Otherwise
    Consumes parsed portions of raw bytearray
    """
    size = len(bom)
    while True:
        if len(raw) >= size:  # enough bytes for bom
            if raw[:size] == bom: # bom present
                del raw[:size]
                (yield bom)
                break
            (yield raw[0:0])  # bom not present so yield empty bytearray
            break
        (yield None)  # not enough bytes yet
    return

class EventSource(object):
    """
    Server Sent Event Stream parser
    """
    Bom = codecs.BOM_UTF8 # utf-8 encoded bom b'\xef\xbb\xbf'

    def __init__(self, raw=None, events=None, jsoned=False):
        """
        Initialize Instance
        raw must be bytearray
        IF events is not None then used passed in deque
            .events will be deque of event odicts
        IF jsoned then deserialize event data as json

        """
        self.raw = raw if raw is not None else bytearray()
        self.events = events if events is not None else deque()
        self.jsoned = True if jsoned else False

        self.parser = None
        self.leid = None  # last event id
        self.bom = None  # bom if any
        self.retry = None  # reconnection time in milliseconds
        self.ended = None
        self.closed = None

        self.makeParser()

    def close(self):
        """
        Assign True to .closed
        """
        self.closed = True

    def parseEvents(self):
        """
        Generator to parse events from .raw bytearray and append to .events
        Each event is odict with the following items:
             id: event id utf-8 decoded or empty
           name: event name utf-8 decoded or empty
           data: event data utf-8 decoded
           json: event data deserialized to odict when applicable pr None

        assigns .retry if any

        Yields None If waiting for more bytes
        Yields True When done


        event         = *( comment / field ) end-of-line
        comment       = colon *any-char end-of-line
        field         = 1*name-char [ colon [ space ] *any-char ] end-of-line
        end-of-line   = ( cr lf / cr / lf / eof )
        eof           = < matches repeatedly at the end of the stream >
        lf            = \n 0xA
        cr            = \r 0xD
        space         = 0x20
        colon         = 0x3A
        bom           = \uFEFF when encoded as utf-8 b'\xef\xbb\xbf'
        name-char     = a Unicode character other than LF, CR, or :
        any-char      = a Unicode character other than LF or CR
        Event streams in this format must always be encoded as UTF-8. [RFC3629]
        """
        eid = self.leid
        ename = u''
        edata = u''
        parts = []
        ejson = None
        lineParser = parseLine(raw=self.raw, eols=(CRLF, LF, CR ), kind="event line")
        while True:
            line = next(lineParser)
            if line is None:
                (yield None)
                continue

            if not line or self.closed:  # empty line or closed so attempt dispatch
                if parts:
                    edata = u'\n'.join(parts)
                if edata:  # data so dispatch event by appending to .events
                    if self.jsoned:
                        try:
                            ejson = json.loads(edata, encoding='utf-8', object_pairs_hook=odict)
                        except ValueError as ex:
                            ejson = None
                        else:  # valid json so null out edata
                            edata = None

                    self.events.append(odict([('id', eid),
                                              ('name', ename),
                                              ('data', edata),
                                              ('json', ejson)]))
                if self.closed:  # all done
                    lineParser.close()  # close generator
                    break
                ename = u''
                edata = u''
                parts = []
                ejson = None
                continue  # parse another event if any

            field, sep, value = line.partition(b':')
            if sep:  # has colon
                if not field:  # comment so ignore
                    # may need to update retry timer here
                    continue

            field = field.decode('UTF-8')
            if value and value[0:1] == b' ':
                del value[0]
            value = value.decode('UTF-8')

            if field == u'event':
                ename = value
            elif field == u'data':
                parts.append(value)
            elif field == u'id':
                self.leid = eid = value
            elif field == u'retry':  #
                try:
                    value = int(value)
                except ValueError as ex:
                    pass  # ignore
                else:
                    self.retry = value

        (yield (eid, ename, edata))
        return

    def parseEventStream(self):
        """
        Generator to parse event stream from .raw bytearray stream
        appends each event to .events deque.
        assigns .bom if any
        assigns .retry if any
        Parses until connection closed

        Each event is odict with the following items:
              id: event id utf-8 decoded or empty
            name: event name utf-8 decoded or empty
            data: event data utf-8 decoded
            json: event data deserialized to odict when applicable pr None

        Yields None If waiting for more bytes
        Yields True When completed and sets .ended to True
        If BOM present at beginning of event stream then assigns to .bom and
        deletes.
        Consumes bytearray as it parses

        stream        = [ bom ] *event
        event         = *( comment / field ) end-of-line
        comment       = colon *any-char end-of-line
        field         = 1*name-char [ colon [ space ] *any-char ] end-of-line
        end-of-line   = ( cr lf / cr / lf / eof )
        eof           = < matches repeatedly at the end of the stream >
        lf            = \n 0xA
        cr            = \r 0xD
        space         = 0x20
        colon         = 0x3A
        bom           = \uFEFF when encoded as utf-8 b'\xef\xbb\xbf'
        name-char     = a Unicode character other than LF, CR, or :
        any-char      = a Unicode character other than LF or CR
        Event streams in this format must always be encoded as UTF-8. [RFC3629]
        """
        self.bom = None
        self.retry = None
        self.leid = None
        self.ended = None
        self.closed = None

        bomParser = parseBom(raw=self.raw, bom=self.Bom)
        while True:  # parse bom if any
            bom = next(bomParser)
            if bom is not None:
                bomParser.close()  # close generator
                self.bom = bom.decode('UTF-8')
                break

            if self.closed:  # no more data so finish
                bomParser.close()
                break
            (yield None)

        eventsParser = self.parseEvents()
        while True:  # parse event(s) so far if any
            result = next(eventParser)
            if result is not None:
                eventsParser.close()
                break
            (yield None)

        (yield True)
        return

    def makeParser(self, raw=None):
        """
        Make event stream parser generator and assign to .parser
        Assign msg to .msg If provided
        """
        if raw:
            self.raw = raw
        self.parser = self.parseEvents()  # make generator

    def parse(self):
        """
        Service the event stream parsing
        must call .makeParser to setup parser
        When done parsing,
           .parser is None
           .ended is True
        """
        if self.parser:
            result = next(self.parser)
            if result is not None:
                self.parser.close()
                self.parser = None


class Respondent(object):
    """
    Nonblocking HTTP Response class
    """

    def __init__(self,
                 msg=None,
                 method=u'GET',
                 jsoned=None,
                 events=None,
                 wlog=None,):
        """
        Initialize Instance
        msg must be bytearray

        msg = bytearray of response msg to parse
        method = request method verb
        jsoned = Boolean flag if response body is expected to be json
        events = deque of events if any
        wlog = WireLog instance if any
        """
        self.msg = msg if msg is not None else bytearray()
        self.method = method.upper() if method else u'GET'
        self.jsoned = True if jsoned else False  # is body json
        self.events = events if events is not None else deque()
        self.wlog = wlog

        self.parser = None  # response parser generator
        self.eventSource = None  # EventSource instance when .evented

        self.headers = None
        self.body = bytearray()  # body data
        self.events = deque()  # events if evented
        self.data = None
        self.parms = None  # chunked encoding extension parameters
        self.trails = None  # chunked encoding trailing headers

        self.version = None # HTTP-Version from status line
        self.status = None  # Status-Code from status line
        self.reason = None  # Reason-Phrase from status line

        self.length = None     # content length of body in response

        self.chunked = None    # is transfer encoding "chunked" being used?
        self.evented = None   # are server sent events being used

        self.persisted = None   # persist connection until server closes
        self.headed = None    # head completely parsed
        self.bodied =  None   # body completely parsed
        self.ended = None     # response from server has ended no more remaining
        self.closed = None  # True when connection closed

        self.makeParser(msg=msg)

    def reinit(self,
               msg=None,
               method=u'GET',
               jsoned=None):
        """
        Reinitialize Instance
        msg must be bytearray

        msg = bytearray of response msg to parse
        method = request method verb
        jsoned = Boolean flag if response body is expected to be json

        """
        if msg is not None:
            self.msg = msg
        if method is not None:
            self.method = method.upper()
        if jsoned is not None:
            self.jsoned = True if jsoned else False

    def close(self):
        """
        Assign True to .closed
        """
        self.closed = True
        if self.eventSource:  # assign True to .eventSource.closed
            self.eventSource.close()

    def parseStatus(self, line):
        """
        Parse the status line from the response
        """
        line = line.decode("iso-8859-1")
        if not line:
            # Presumably, the server closed the connection before
            # sending a valid response.
            raise BadStatusLine(line)
        try:
            if sys.version > '3':
                version, status, reason = line.split(maxsplit=2)
            else:
                version, status, reason = line.split()
        except ValueError:
            try:
                if sys.version > '3':
                    version, status = line.split(maxsplit1=1)
                else:
                    version, status = line.split()
                reason = ""
            except ValueError:
                # empty version will cause next test to fail.
                version = ""
        if not version.startswith("HTTP/"):
            raise BadStatusLine(line)

        # The status code is a three-digit number
        try:
            status = int(status)
            if status < 100 or status > 999:
                raise BadStatusLine(line)
        except ValueError:
            raise BadStatusLine(line)
        return (version, status, reason)

    def checkPersisted(self):
        """
        Checks headers to determine if connection should be kept open until
        server closes it
        Sets the .persisted flag
        """
        connection = self.headers.get("connection")  # check connection header
        if self.version == 11:  # rules for http v1.1
            self.persisted = True  # connections default to persisted
            # An HTTP/1.1 proxy is assumed to stay open unless
            # explicitly closed.
            connection = self.headers.get("connection")
            if connection and "close" in connection.lower():
                self.persisted = False

            # non-chunked but persistent connections should have non None for
            # content-length Otherwise assume not persisted
            elif (not self.chunked and self.length is None):
                self.persisted = False

        elif self.version == 10:
            self.persisted = False  # connections default to non-persisted
            # Some HTTP/1.0 implementations have support for persistent
            # connections, using rules different than HTTP/1.1.

            if self.evented:  # server sent events
                self.persisted = True

            # For older HTTP, Keep-Alive indicates persistent connection.
            elif self.headers.get("keep-alive"):
                self.persisted = True

            # At least Akamai returns a "Connection: Keep-Alive" header,
            # which was supposed to be sent by the client.
            elif connection and "keep-alive" in connection.lower():
                self.persisted = True

            else:  # Proxy-Connection is a netscape hack.
                proxy = self.headers.get("proxy-connection")
                if proxy and "keep-alive" in proxy.lower():
                    self.persisted = True

    def parseLine(self, eols=(CRLF, ), kind="header line"):
        """
        Generator to parse  http line from self.msg
        Each line demarcated by one of eols
        Yields None If waiting for more to parse
        Yields line Otherwise

        Raise error if eol not found before  MAX_LINE_SIZE
        """
        while True:
            for eol in eols:  # loop over eols unless found
                index = self.msg.find(eol)  # not found index == -1
                if index >= 0:
                    break

            if index < 0:  # not found
                if len(self.msg) > MAX_LINE_SIZE:
                    raise LineTooLong(kind)
                else:
                    (yield None)  # more data needed not done parsing header
                    continue

            if index > MAX_LINE_SIZE:  # found but line too long
                raise LineTooLong(kind)

            line = self.msg[:index]
            index += len(eol)  # strip eol
            del self.msg[:index] # remove used bytes
            (yield line)
        return

    def parseLeader(self, eols=(CRLF, LF), kind="leader header line"):
        """
        Generator to parse entire leader of header lines from self.msg
        Each line demarcated by one of eols
        Yields None If more to parse
        Yields lines Otherwise as indicated by empty line

        Raise error if eol not found before  MAX_LINE_SIZE
        """
        lines = []
        while True:  # loop until entire heading indicated by empty line
            for eol in eols:  # loop over eols unless found
                index = self.msg.find(eol)  # not found index == -1
                if index >= 0:
                    break

            if index < 0:  # not found
                if len(self.msg) > MAX_LINE_SIZE:
                    raise LineTooLong(kind)
                else:
                    (yield None)  # more data needed not done parsing header
                    continue

            if index > MAX_LINE_SIZE:  # found but line too long
                raise LineTooLong(kind)

            line = self.msg[:index]
            index += len(eol)  # strip eol
            del self.msg[:index] # remove used bytes
            lines.append(line)

            if len(lines) > MAX_HEADERS:
                raise HTTPException("got more than {0} headers".format(MAX_HEADERS))

            if not line:  # empty line so entire heading done
                (yield lines) # heading done
        return

    def parseHead(self):
        """
        Generator to parse headers in heading of .msg
        Yields None if more to parse
        Yields True if done parsing
        """
        if self.headed:
            return  # already parsed the head

        # create generator
        lineParser = self.parseLine(eols=(CRLF, LF), kind="status line")
        while True:  # parse until we get a non-100 status
            line = next(lineParser)
            if line is None:
                (yield None)
                continue
            lineParser.close()  # close generator

            version, status, reason = self.parseStatus(line)
            if status != CONTINUE:  # 100 continue (with request or ignore)
                break

            leaderParser = self.parseLeader(eols=(CRLF, LF), kind="continue header line")
            while True:
                lines = next(leaderParser)
                if lines is not None:
                    leaderParser.close()
                    break
                (yield None)

        self.code = self.status = status
        self.reason = reason.strip()
        if version in ("HTTP/1.0", "HTTP/0.9"):
            # Some servers might still return "0.9", treat it as 1.0 anyway
            self.version = 10
        elif version.startswith("HTTP/1."):
            self.version = 11   # use HTTP/1.1 code for HTTP/1.x where x>=1
        else:
            raise UnknownProtocol(version)

        leaderParser = self.parseLeader(eols=(CRLF, LF), kind="leader header line")
        while True:
            lines = next(leaderParser)
            if lines is not None:
                leaderParser.close()
                break
            (yield None)

        self.headers = lodict()
        if lines:
            #email Parser wants to see strings rather than bytes.
            #So convert bytes to string
            lines.extend((bytearray(b''), bytearray(b'')))  # add blank line for HeaderParser
            hstring = bytearray(CRLF).join(lines).decode('iso-8859-1')
            self.headers.update(HeaderParser().parsestr(hstring).items())

        # are we using the chunked-style of transfer encoding?
        transferEncoding = self.headers.get("transfer-encoding")
        if transferEncoding and transferEncoding.lower() == "chunked":
            self.chunked = True
        else:
            self.chunked = False

        # NOTE: RFC 2616, S4.4, #3 says ignore if transfer-encoding is "chunked"
        contentLength = self.headers.get("content-length")
        if contentLength and not self.chunked:
            try:
                self.length = int(contentLength)
            except ValueError:
                self.length = None
            else:
                if self.length < 0:  # ignore nonsensical negative lengths
                    self.length = None
        else:
            self.length = None

        # does the body have a fixed length? (of zero)
        if ((self.status == NO_CONTENT or self.status == NOT_MODIFIED) or
                (100 <= self.status < 200) or      # 1xx codes
                (self.method == "HEAD")):
            self.length = 0

        contentType = self.headers.get("content-type")
        if contentType and contentType.lower() == 'text/event-stream':
            self.evented = True
            self.eventSource = EventSource(raw=self.body,
                                           events=self.events,
                                           jsoned=self.jsoned)
        else:
            self.evented = False

        # Should connection be kept open until server closes
        self.checkPersisted()  # sets .persisted

        self.headed = True
        yield True
        return

    def parseChunk(self):  # reading transfer encoded
        """
        Generator to parse next chunk
        Yields None If waiting for more bytes
        Yields tuple (size, parms, trails, chunk) Otherwise
        Where:
            size is int size of the chunk
            parms is dict of chunk extension parameters
            trails is dict of chunk trailer headers (only on last chunk if any)
            chunk is chunk if any or empty if not

        Chunked-Body   = *chunk
                    last-chunk
                    trailer
                    CRLF
        chunk          = chunk-size [ chunk-extension ] CRLF
                         chunk-data CRLF
        chunk-size     = 1*HEX
        last-chunk     = 1*("0") [ chunk-extension ] CRLF
        chunk-extension= *( ";" chunk-ext-name [ "=" chunk-ext-val ] )
        chunk-ext-name = token
        chunk-ext-val  = token | quoted-string
        chunk-data     = chunk-size(OCTET)
        trailer        = *(entity-header CRLF)
        """
        size = 0
        parms = odict()
        trails = odict()
        chunk = bytearray()

        lineParser = self.parseLine(eols=(CRLF, ), kind="chunk size line")
        while True:
            line = next(lineParser)
            if line is not None:
                lineParser.close()  # close generator
                break
            (yield None)

        size, sep, exts = line.partition(b';')
        try:
            size = int(size.strip().decode('ascii'), 16)
        except ValueError:  # bad size
            raise

        if exts:  # parse extensions parameters
            exts = exts.split(b';')
            for ext in exts:
                ext = ext.strip()
                name, sep, value = ext.partition(b'=')
                parms[name.strip()] = value.strip() or None

        if size == 0:  # last chunk so parse trailing headers
            trails = self.parseHeaders(kind="trailer header line")
        else:
            while len(self.msg) < size:  # need more for chunk
                (yield None)

            chunk = self.msg[:size]
            del self.msg[:size]  # remove used bytes

            lineParser = self.parseLine(eols=(CRLF, ), kind="chunk end line")
            while True:
                line = next(lineParser)
                if line is not None:
                    lineParser.close()  # close generator
                    break
                (yield None)

            if line:  # not empty so raise error
                raise ValueError("Chunk end error. Expected empty got "
                         "'{0}' instead".format(line.decode('iso-8859-1')))

        (yield (size, parms, trails, chunk))
        return

    def parseBody(self):
        """
        Parse body
        """
        if self.bodied:
            return  # already parsed the body

        if self.length and self.length < 0:
            raise ValueError("Invalid content length of {0}".format(self.length))

        del self.body[:]  # clear body
        #self.events.clear()  # clear events

        if self.chunked:  # chunked takes precedence over length
            self.parms = odict()
            while True:  # parse all chunks here
                chunkParser = self.parseChunk()
                while True:  # parse another chunk
                    result = next(chunkParser)
                    if result is not None:
                        chunkParser.close()
                        break
                    (yield None)

                size, parms, trails, chunk = result

                if parms:  # chunk extension parms
                    self.parms.update(parms)

                if size:  # size non zero so append chunk but keep iterating
                    self.body.extend(chunk)
                    if self.evented:
                        self.eventSource.parse()  # parse events here

                    if self.closed:  # no more data so finish
                        chunkParser.close()
                        break

                else:  # last chunk when empty chunk so done
                    if trails:
                        self.trails = trails
                    chunkParser.close()
                    break

        elif self.length != None:  # known content length
            while len(self.msg) < self.length:
                (yield None)

            self.body = self.msg[:self.length]
            del self.msg[:self.length]

        else:  # unknown content length so parse forever until closed
            while True:
                if self.msg:
                    self.body.extend(self.msg[:])
                    del self.msg[:len(self.msg)]

                if self.evented:
                    self.eventSource.parse()  # parse events here

                if self.closed:  # no more data so finish
                    break

                (yield None)

        self.bodied = True
        (yield True)
        return

    def parseResponse(self):
        """
        Generator to parse response bytearray.
        Parses msg if not None
        Otherwise parse .msg

        """
        self.headed = False
        self.bodied = False
        self.ended = False
        self.closed = False

        headParser = self.parseHead()
        while True:
            result = next(headParser)
            if result is not None:
                headParser.close()
                break
            (yield None)

        bodyParser = self.parseBody()
        while True:
            result = next(bodyParser)
            if result is not None:
                bodyParser.close()
                break
            (yield None)

        self.ended = True
        (yield True)
        return

    def makeParser(self, msg=None):
        """
        Make response parser generator and assign to .parser
        Assign msg to .msg If provided
        """
        if msg:
            self.msg = msg

        self.parser = self.parseResponse()  # make generator

    def parse(self):
        """
        Service the response parsing
        must call .makeParser to setup parser
        When done parsing,
           .parser is None
           .ended is True

        """
        if self.parser:
            result = next(self.parser)
            if result is not None:
                self.parser.close()
                self.parser = None


class Connector(Outgoer):
    """
    Http Client Connection Manager with Nonblocking support
    Uses Nonblocking TCP Socket Client Class.
    """
    def __init__(self,
                 requester=None,
                 respondent=None,
                 name='',
                 uid=0,
                 bufsize=8096,
                 host='127.0.0.1',
                 port=None,
                 wlog=None,
                 method=u'GET',  # unicode
                 url=u'/',  # unicode
                 headers=None,
                 body=b'',
                 msg=None,
                 jsoned=None,
                 events=None,
                 requests=None,
                 responses=None,
                 **kwa):
        """
        Initialization method for instance.
        requester = instance of Requester or None
        respondent = instance of Respondent or None

        if either of requester, respondent instances are not provided (None)
        some or all of these parameters will be used for initialization

        name = user friendly name for connection
        uid = unique identifier for connection
        host = host address of remote server
        port = socket port of remote server
        bufsize = buffer size

        method = http request method verb unicode
        url = http url unicode
        headers = dict of http headers
        body = byte or binary array of request body bytes or bytearray
        msg = bytearray of response msg to parse
        jsoned = Boolean flag if response body is expected to be json
        events = deque of events if any
        wlog = WireLog instance if any
        """
        # .requests is deque of dicts of request data
        self.requests = requests if requests is not None else deque()
        # .responses is deque of dicts of response data
        self.responses = responses if responses is None else deque()
        # .events is deque of dicts of response server sent event data
        self.events = events if events is not None else deque()
        self.waited = False  # Boolean True If sent request but waiting for response

        host, port = normalizeHostPort(host, port, defaultPort=80)

        super(Connector, self).__init__(name=name,
                                        uid=uid,
                                        ha=(host, port),
                                        bufsize=bufsize,
                                        wlog=wlog,
                                        **kwa)

        if requester is None:
            requester = Requester(host=host,
                                  port=port,
                                  method=method,
                                  url=url,  # unicode
                                  headers=headers,
                                  body=body,)
        else:
            if requester.host != host:
                requester.host = host
            if requester.port != port:
                requester.port = port
            requester.reinit(method=method, url=url, headers=headers, body=body)
        self.requester = requester

        if respondent is None:
            respondent = Respondent(msg=self.rxbs,
                                    method=method,
                                    jsoned=jsoned,
                                    events=self.events,
                                    wlog=wlog,)
        else:
            respondent.reinit(method=method, jsoned=jsoned)
        self.respondent = respondent

    def reinit(self,
               method=None,
               url=None,
               headers=None,
               body=None,
               jsoned=None):
        """
        Reinit to send another request and process response
        """
        self.requester.reinit(method=method, url=url, headers=headers, body=body)
        self.respondent.reinit(method=method, jsoned=jsoned)

    def request(self, method=None, url=None, headers=None, body=None):
        """
        Build and transmit request
        """
        self.waited = True
        self.transmit(self.requester.build(method=method,
                                           url=url,
                                           headers=headers,
                                           body=body))

    def serviceResponse(self):
        """
        Service Rx on connection and parse
        """
        self.serviceAllRx()
        self.respondent.parse()
        if self.respondent.ended:
            self.waited = False



    def serviceRequestResponse(self):
        """
        Service request response
        """
        self.serviceTxes()
        self.serviceAllRx()
        self.respondent.parse()
