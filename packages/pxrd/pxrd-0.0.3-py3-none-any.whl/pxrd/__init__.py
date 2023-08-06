from pxrd.pxread import __version__, PxFile


def read(filename):
    with open(filename, 'rt') as f:
        px = PxFile.from_string(f.read())
    return px


def reads(s):
    px = PxFile.from_string(s)
    return px