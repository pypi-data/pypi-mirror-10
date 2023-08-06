#!/usr/bin/env python3
import contextlib
import io
import sixer
import sys
import tempfile
import textwrap
import unittest


@contextlib.contextmanager
def replace_stdout():
    old_stdout = sys.stdout
    try:
        buffer = io.StringIO()
        sys.stdout = buffer
        yield buffer
    finally:
        sys.stdout = old_stdout


class TestOperations(unittest.TestCase):
    # TODO: test Patcher.walk

    def check(self, operation, before, after, **kw):
        before = textwrap.dedent(before).strip()
        after = textwrap.dedent(after).strip()

        self.patcher = sixer.Patcher('.', (operation,))
        for attr, value in kw.items():
            setattr(self.patcher, attr, value)

        with tempfile.NamedTemporaryFile("w+") as temp:
            temp.write(before)
            temp.flush()
            with replace_stdout():
                self.patcher.patch(temp.name)
            temp.seek(0)
            code = temp.read()

        self.assertEqual(code, after)

    def check_unchanged(self, operation, code):
        self.check(operation, code, code)

    def test_raise2(self):
        self.check("raise",
            "raise Exception, 'message'",
            "raise Exception('message')")

    def test_raise3(self):
        self.check("raise",
            "raise a, b, c",
            """
            import six

            six.reraise(a, b, c)
            """)

    def test_reraise(self):
        self.check("raise",
            "raise exc[0], exc[1], exc[2]",
            """
            import six

            six.reraise(*exc)
            """)

    def test_xrange(self):
        self.check("xrange",
            "for i in xrange(10): pass",
            "for i in range(10): pass")

        self.check("xrange",
            "for i in xrange(n): pass",
            """
            from six.moves import range

            for i in range(n): pass
            """)

        self.check("xrange",
            "for i in xrange(10): pass",
            """
            from six.moves import range

            for i in range(10): pass
            """, max_range=5)

    def test_unicode(self):
        self.check("unicode",
            "value = unicode(data)",
            """
            import six

            value = six.text_type(data)
            """)

    def test_add_six_import(self):
        # only stdlib
        self.check("unicode",
            """
            import copy

            t = unicode
            """,
            """
            import copy

            import six

            t = six.text_type
            """)

        # only third party
        self.check("unicode",
            """
            import oslo_utils

            t = unicode
            """,
            """
            import oslo_utils
            import six

            t = six.text_type
            """)

        # stdlib+third party
        self.check("unicode",
            """
            import copy

            import oslo_utils

            t = unicode
            """,
            """
            import copy

            import oslo_utils
            import six

            t = six.text_type
            """)

        # only application
        self.check("unicode",
            """
            import nova

            t = unicode
            """,
            """
            import six

            import nova

            t = six.text_type
            """)

    def test_unicode_unchanged(self):
        self.check_unchanged("unicode",
            """
            import unicodedata

            # unicode in comments

            def test_unicode():
                pass
            """)

    def test_iteritems(self):
        self.check("iteritems",
            "for key, value in data.iteritems(): pass",
            """
            import six

            for key, value in six.iteritems(data): pass
            """)

    def test_iteritems_expr(self):
        self.check("iteritems",
            """
            items = obj.data[0].attr.iteritems()
            """,
            """
            import six

            items = six.iteritems(obj.data[0].attr)
            """)

    def test_itervalues(self):
        self.check("itervalues",
            "for value in data.itervalues(): pass",
            """
            import six

            for value in six.itervalues(data): pass
            """)

    def test_iterkeys(self):
        self.check("iterkeys",
            "for value in data.iterkeys(): pass",
            """
            import six

            for value in six.iterkeys(data): pass
            """)

    def test_next(self):
        self.check("next",
            "item = gen.next()",
            "item = next(gen)")

        self.check("next",
            "item = (x+1 for x in data).next()",
            "item = next(x+1 for x in data)")

        self.check("next",
            "item = ((x * 2) for x in data).next()",
            "item = next((x * 2) for x in data)")

    def test_long(self):
        self.check("long",
            "values = (0L, 1L, 12L, 123L, 1234L, 12345L)",
            "values = (0, 1, 12, 123, 1234, 12345)")

        # octal numbers are unchanged
        self.check_unchanged("long",
            "values = (00L, 01L, 012L, 0123L, 01234L, 012345L)")

    def test_basestring(self):
        self.check("basestring",
            "isinstance(foo, basestring)",
            """
            import six

            isinstance(foo, six.string_types)
            """)

    def test_six_moves_import(self):
        self.check("six_moves",
            """
            import __builtin__

            __builtin__.open()
            """,
            """
            from six.moves import builtins

            builtins.open()
            """)

    def test_six_moves_from_import(self):
        self.check("six_moves",
            "from __builtin__ import len, open",
            "from six.moves.builtins import len, open")

    def test_stringio(self):
        self.check("stringio",
            """
            import StringIO

            s = StringIO.StringIO()
            """,
            """
            import six


            s = six.StringIO()
            """)

    def test_urllib(self):
        # urllib2.urlopen, urllib2.URLError
        self.check("urllib",
            """
            import urllib2

            try:
                urllib2.urlopen(url)
            except urllib2.URLError as exc:
                pass
            """,
            """
            from six.moves import urllib


            try:
                urllib.request.urlopen(url)
            except urllib.error.URLError as exc:
                pass
            """)

        # import urllib2
        self.check("urllib",
            """
            import urllib2

            m = urllib2
            """,
            """
            from six.moves import urllib


            m = urllib
            """)

        # don't touch parse_http_list
        self.check_unchanged("urllib",
            """
            urllib2.parse_http_list()
            """)

    def test_all(self):
        self.check("all",
            """
            values = (0L, 1L, 12L, 123L, 1234L, 12345L)

            for i in xrange(10): pass
            """,
            """
            values = (0, 1, 12, 123, 1234, 12345)

            for i in range(10): pass
            """)


if __name__ == "__main__":
    unittest.main()
