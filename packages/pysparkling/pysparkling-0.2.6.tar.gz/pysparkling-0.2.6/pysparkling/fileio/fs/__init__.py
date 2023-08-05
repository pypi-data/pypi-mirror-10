from __future__ import absolute_import

from .file_system import FileSystem
from .local import Local
from .s3 import S3


FILE_EXTENSIONS = [
    (('file', ''), Local),
    (('s3', 's3n'), S3),
]


def get_fs(path):
    """Find the file system implementation for this path."""
    scheme = ''

    if '://' in path:
        scheme = path[:path.find('://')]

    for schemes, fs_class in FILE_EXTENSIONS:
        if scheme in schemes:
            return fs_class

    return FileSystem
