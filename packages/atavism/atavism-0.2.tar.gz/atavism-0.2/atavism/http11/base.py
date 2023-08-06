import re
from atavism.http11.content import Content
from atavism.http11.headers import Headers
from atavism.http11.range import Range


class BaseHttp(object):
    """ Base class for other HTTP transactional classes. This class tries
        to provide the core functionality for various classes.
    """
    RANGE_re = re.compile(r"([0-9]+)?-([0-9]+)?,?")

    def __init__(self):
        self.path = ''
        self.http = 'HTTP/1.1'

        self.header = Headers()
        self._content = Content()

        self.headers_sent = False
        self.headers_only = False
        self.ranges = []

    def __len__(self):
        return len(self._content)

    def get(self, key, default=None):
        return self.header.get(key, default)

    def add_header(self, key, val):
        self.header.add_header(key, val)

    def add_headers(self, hdr_dict):
        self.header.add_headers(hdr_dict)

    ### Connection Information
    @property
    def is_keepalive(self):
        return False if self.header.get('connection', '').lower() == 'close' else True

    def send_complete(self):
        ct = self._content
        while ct._next is not None:
            ct = ct._next
        if self.headers_sent and ct.send_complete:
            return True
        return False

    def next_output(self):
        data = b''
        if not self.headers_sent:
            data += str(self.header).encode()
            self.headers_sent = True
        if self.headers_only:
            self._content.finished = True
            return data

        data += self._content.next(len(data))
        return data

    ### Ranges
    def parse_ranges(self, key):
        """ Parse a range request into individual byte ranges. """
        self.ranges = []
        poss = self.get(key)
        if poss is None or poss.lower() == 'none':
            return
        if not poss.startswith("bytes="):
            return
        matches = self.RANGE_re.findall(poss[6:])
        for m in matches:
            self.ranges.append(Range(m))

    def add_range(self, start=None, end=None):
        if start is None and end is None:
            return
        self.ranges.append(Range((start, end)))

    def has_ranges(self):
        return len(self.ranges) > 0

    def set_ranges(self, ranges):
        self.ranges = ranges

    ### Content

    @property
    def content(self):
        return self._content.content

    def decoded_content(self):
        return self._content.decoded_content()

    def set_content(self, cntnt_obj):
        self._content = cntnt_obj

    def set_content_type(self, ct):
        self._content.content_type = ct

    def read_content(self, cntnt):
        r = 0
        if not self.header.finished:
            r = self.header.read_content(cntnt)
            if self.header.finished:
                self._update_content()
        r += self._content.read_content(cntnt[r:])
        return r

    def _update_content(self):
        self._content.content_type = self.header.get('content-type')
        te = self.get('transfer-encoding')
        cl = self.get('content-length')
        # Set how we will detect the length of content...
        if te is not None and te.lower() == 'chunked':
            self._content.content_sz = 'chunked'
        elif cl is not None:
            self._content.content_sz = cl
        else:
            self._content.content_sz = None

        rngs = self.get('range')
        if rngs is not None:
            self.parse_ranges('range')

        ce = self.get('content-encoding')
        if ce is not None and ce.lower() != 'identity':
            self._content.set_compression(ce)

    def set_compression(self, method):
        self._content.set_compression(method)

    def _complete(self):
        """ Record that the creation of a response/request is complete. """
        self._content.finished = True
        self._content.compress()
        self.header.add_headers(self._content.header_lines())

    def is_complete(self):
        """ Has the entire input stream been seen?
        :return: True or False
        """
        if self.header.finished is False:
            return False
        elif not self.header.needs_content:
            return True
        return self._content.finished

    def add_content(self, cntnt):
        self._content.add_content(cntnt)
