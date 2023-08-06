import mimetypes
import os
from mimetypes import *

try:
    import winreg as _winreg
except ImportError:
    _winreg = None

__all__ = [
    "knownfiles", "inited", "MimeTypes",
    "guess_type", "get_all_extensions", "guess_all_extensions",
    "guess_extension", "add_type", "init", "read_mime_types",
    "suffix_map", "encodings_map", "types_map", "common_types",
    "image_file_extensions", "audio_file_extensions",
    "video_file_extensions"
]

_db = None


class MimeTypes(mimetypes.MimeTypes):
    """MIME-types datastore.

    This datastore can handle information from mime.types-style files
    and supports basic determination of MIME type from a filename or
    URL, and can guess a reasonable extension given a MIME type.
    """

    def get_all_extensions(self, type, strict=True):
        """Get the extensions for a file based on its top-level media type.

        Return value is a list of strings giving the possible filename
        extensions, including the leading dot ('.').  The extension is not
        guaranteed to have been associated with any particular data stream,
        but would be mapped to the MIME type `type' by guess_type().

        Optional `strict' argument when false adds a bunch of commonly found,
        but non-standard types.
        """
        type = type.lower()
        extensions = []
        for ext, mime_type in self.types_map[True].items():
            if mime_type.split('/')[0] == type:
                extensions.append(ext)
        if not strict:
            for ext, mime_type in self.types_map[False].items():
                if ext not in extensions and mime_type.split('/')[0] == type:
                    extensions.append(ext)
        return extensions


def guess_type(url, strict=True):
    """Guess the type of a file based on its URL.

    Return value is a tuple (type, encoding) where type is None if the
    type can't be guessed (no or unknown suffix) or a string of the
    form type/subtype, usable for a MIME Content-type header; and
    encoding is None for no encoding or the name of the program used
    to encode (e.g. compress or gzip).  The mappings are table
    driven.  Encoding suffixes are case sensitive; type suffixes are
    first tried case sensitive, then case insensitive.

    The suffixes .tgz, .taz and .tz (case sensitive!) are all mapped
    to ".tar.gz".  (This is table-driven too, using the dictionary
    suffix_map).

    Optional `strict' argument when false adds a bunch of commonly found, but
    non-standard types.
    """
    if _db is None:
        init()
    return _db.guess_type(url, strict)


def get_all_extensions(type, strict=True):
    """Get the extensions for a file based on its top-level media type.

    Return value is a list of strings giving the possible filename
    extensions, including the leading dot ('.').  The extension is not
    guaranteed to have been associated with any particular data stream,
    but would be mapped to the MIME type `type' by guess_type().

    Optional `strict' argument when false adds a bunch of commonly found,
    but non-standard types.
    """
    if _db is None:
        init()
    return _db.get_all_extensions(type, strict)


def guess_all_extensions(type, strict=True):
    """Guess the extensions for a file based on its MIME type.

    Return value is a list of strings giving the possible filename
    extensions, including the leading dot ('.').  The extension is not
    guaranteed to have been associated with any particular data
    stream, but would be mapped to the MIME type `type' by
    guess_type().  If no extension can be guessed for `type', None
    is returned.

    Optional `strict' argument when false adds a bunch of commonly found,
    but non-standard types.
    """
    if _db is None:
        init()
    return _db.guess_all_extensions(type, strict)


def guess_extension(type, strict=True):
    """Guess the extension for a file based on its MIME type.

    Return value is a string giving a filename extension, including the
    leading dot ('.').  The extension is not guaranteed to have been
    associated with any particular data stream, but would be mapped to the
    MIME type `type' by guess_type().  If no extension can be guessed for
    `type', None is returned.

    Optional `strict' argument when false adds a bunch of commonly found,
    but non-standard types.
    """
    if _db is None:
        init()
    return _db.guess_extension(type, strict)


def add_type(type, ext, strict=True):
    """Add a mapping between a type and an extension.

    When the extension is already known, the new
    type will replace the old one. When the type
    is already known the extension will be added
    to the list of known extensions.

    If strict is true, information will be added to
    list of standard types, else to the list of non-standard
    types.
    """
    if _db is None:
        init()
    return _db.add_type(type, ext, strict)


def init(files=None):
    global suffix_map, types_map, encodings_map, common_types
    global inited, _db
    inited = True  # so that MimeTypes.__init__() doesn't call us again

    if files is None or _db is None:
        db = MimeTypes()
        if _winreg:
            db.read_windows_registry()

        if files is None:
            files = knownfiles
        else:
            files = knownfiles + list(files)
    else:
        db = _db

    for file in files:
        if os.path.isfile(file):
            db.read(file)
    encodings_map = db.encodings_map
    suffix_map = db.suffix_map
    types_map = db.types_map[True]
    common_types = db.types_map[False]
    # Make the DB a global variable now that it is fully initialized
    _db = db


def read_mime_types(file):
    try:
        f = open(file, encoding='utf-8')
    except OSError:
        return None
    with f:
        db = MimeTypes()
        db.readfp(f, True)
        return db.types_map[True]


_default_mime_types = mimetypes._default_mime_types  # so that unittest can find it

image_file_extensions = get_all_extensions('image')
audio_file_extensions = get_all_extensions('audio')
video_file_extensions = get_all_extensions('video')
