import os

from rawkit.libraw import libraw


def discover(path):
    """
    Recursively search for raw files in a given directory.
    :param path: the directory to recursively search
    :type path: :class:`basestring`
    """
    file_list = []
    raw = libraw.libraw_init(0)

    for root, _, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name).encode('ascii')
            if libraw.libraw_open_file(raw, file_path) == 0:
                file_list.append(file_path)
            libraw.libraw_recycle(raw)

    libraw.libraw_close(raw)
    return file_list
