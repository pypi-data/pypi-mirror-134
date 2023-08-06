import locale
import pathlib
import sys
import unittest
from test import test_mimetypes, support

from mimetypes_extensions import mimetypes_extensions


def setUpModule():
    global knownfiles
    knownfiles = mimetypes_extensions.knownfiles

    # Tell it we don't know about external files:
    mimetypes_extensions.knownfiles = []
    mimetypes_extensions.inited = False
    mimetypes_extensions._default_mime_types()


def tearDownModule():
    # Restore knownfiles to its initial state
    mimetypes_extensions.knownfiles = knownfiles


class MimeTypesTestCase(test_mimetypes.MimeTypesTestCase):
    def setUp(self):
        self.db = mimetypes_extensions.MimeTypes()

    def test_read_mime_types(self):
        eq = self.assertEqual

        # Unreadable file returns None
        self.assertIsNone(mimetypes_extensions.read_mime_types("non-existent"))

        with support.temp_dir() as directory:
            data = "x-application/x-unittest pyunit\n"
            file = pathlib.Path(directory, "sample.mimetype")
            file.write_text(data)
            mime_dict = mimetypes_extensions.read_mime_types(file)
            eq(mime_dict[".pyunit"], "x-application/x-unittest")

        # bpo-41048: read_mime_types should read the rule file with 'utf-8' encoding.
        # Not with locale encoding. _bootlocale has been imported because io.open(...)
        # uses it.
        with support.temp_dir() as directory:
            data = "application/no-mans-land  Fran\u00E7ais"
            file = pathlib.Path(directory, "sample.mimetype")
            file.write_text(data, encoding='utf-8')
            import _bootlocale
            with support.swap_attr(_bootlocale, 'getpreferredencoding', lambda do_setlocale=True: 'ASCII'):
                mime_dict = mimetypes_extensions.read_mime_types(file)
            eq(mime_dict[".Français"], "application/no-mans-land")

    def test_get_all_extensions(self):
        unless = self.assertTrue
        get_all_extensions = mimetypes_extensions.get_all_extensions
        mimetypes_extensions.add_type('foo/bar', '.strictfoobar', strict=True)
        mimetypes_extensions.add_type('foo/bar', '.nonstrictfoobar', strict=False)
        # First try strict
        unless('.strictfoobar' in get_all_extensions('foo', strict=True))
        unless('.nonstrictfoobar' not in get_all_extensions('foo', strict=True))
        # And then non-strict
        unless('.strictfoobar' in get_all_extensions('foo', strict=False))
        unless('.nonstrictfoobar' in get_all_extensions('foo', strict=False))
        # Reinitialize
        mimetypes_extensions.init()

    def test_encoding(self):
        getpreferredencoding = locale.getpreferredencoding
        self.addCleanup(setattr, locale, 'getpreferredencoding',
                        getpreferredencoding)
        locale.getpreferredencoding = lambda: 'ascii'

        filename = support.findfile("mime.types")
        mimes = mimetypes_extensions.MimeTypes([filename])
        exts = mimes.guess_all_extensions('application/vnd.geocube+xml',
                                          strict=True)
        self.assertEqual(exts, ['.g3', '.g\xb3'])

    def test_init_reinitializes(self):
        # Issue 4936: make sure an init starts clean
        # First, put some poison into the types table
        mimetypes_extensions.add_type('foo/bar', '.foobar')
        self.assertEqual(mimetypes_extensions.guess_extension('foo/bar'), '.foobar')
        # Reinitialize
        mimetypes_extensions.init()
        # Poison should be gone.
        self.assertEqual(mimetypes_extensions.guess_extension('foo/bar'), None)

    def test_preferred_extension(self):
        def check_extensions():
            self.assertEqual(mimetypes_extensions.guess_extension('application/octet-stream'), '.bin')
            self.assertEqual(mimetypes_extensions.guess_extension('application/postscript'), '.ps')
            self.assertEqual(mimetypes_extensions.guess_extension('application/vnd.apple.mpegurl'), '.m3u')
            self.assertEqual(mimetypes_extensions.guess_extension('application/vnd.ms-excel'), '.xls')
            self.assertEqual(mimetypes_extensions.guess_extension('application/vnd.ms-powerpoint'), '.ppt')
            self.assertEqual(mimetypes_extensions.guess_extension('application/x-texinfo'), '.texi')
            self.assertEqual(mimetypes_extensions.guess_extension('application/x-troff'), '.roff')
            self.assertEqual(mimetypes_extensions.guess_extension('application/xml'), '.xsl')
            self.assertEqual(mimetypes_extensions.guess_extension('audio/mpeg'), '.mp3')
            self.assertEqual(mimetypes_extensions.guess_extension('image/jpeg'), '.jpg')
            self.assertEqual(mimetypes_extensions.guess_extension('image/tiff'), '.tiff')
            self.assertEqual(mimetypes_extensions.guess_extension('message/rfc822'), '.eml')
            self.assertEqual(mimetypes_extensions.guess_extension('text/html'), '.html')
            self.assertEqual(mimetypes_extensions.guess_extension('text/plain'), '.txt')
            self.assertEqual(mimetypes_extensions.guess_extension('video/mpeg'), '.mpeg')
            self.assertEqual(mimetypes_extensions.guess_extension('video/quicktime'), '.mov')

        check_extensions()
        mimetypes_extensions.init()
        check_extensions()

    def test_init_stability(self):
        mimetypes_extensions.init()

        suffix_map = mimetypes_extensions.suffix_map
        encodings_map = mimetypes_extensions.encodings_map
        types_map = mimetypes_extensions.types_map
        common_types = mimetypes_extensions.common_types

        mimetypes_extensions.init()
        self.assertIsNot(suffix_map, mimetypes_extensions.suffix_map)
        self.assertIsNot(encodings_map, mimetypes_extensions.encodings_map)
        self.assertIsNot(types_map, mimetypes_extensions.types_map)
        self.assertIsNot(common_types, mimetypes_extensions.common_types)
        self.assertEqual(suffix_map, mimetypes_extensions.suffix_map)
        self.assertEqual(encodings_map, mimetypes_extensions.encodings_map)
        self.assertEqual(types_map, mimetypes_extensions.types_map)
        self.assertEqual(common_types, mimetypes_extensions.common_types)


@unittest.skipUnless(sys.platform.startswith("win"), "Windows only")
class Win32MimeTypesTestCase(test_mimetypes.Win32MimeTypesTestCase):
    def setUp(self):
        # ensure all entries actually come from the Windows registry
        self.original_types_map = mimetypes_extensions.types_map.copy()
        mimetypes_extensions.types_map.clear()
        mimetypes_extensions.init()
        self.db = mimetypes_extensions.MimeTypes()

    def tearDown(self):
        # restore default settings
        mimetypes_extensions.types_map.clear()
        mimetypes_extensions.types_map.update(self.original_types_map)


class MiscTestCase(test_mimetypes.MiscTestCase):
    def test__all__(self):
        support.check__all__(self, mimetypes_extensions)


if __name__ == "__main__":
    unittest.main()
