"""MakeAboveMeme

Usage:
    makeAboveMeme.py [-hv]

Options:
    -h --help       Show this help message.
    -v --version    Show the current version.

"""
from docopt import docopt

VERSION = 0.1

if __name__ == '__main__':
    arguments = docopt(__doc__, version="MakeAboveMeme {0}".format(VERSION))
    print(arguments)
