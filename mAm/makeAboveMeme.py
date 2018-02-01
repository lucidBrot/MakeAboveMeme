#!/usr/bin/env python
"""MakeAboveMeme

Usage:
    makeAboveMeme.py (-h | -v)
    makeAboveMeme.py [-T <title>] [-t <text>] [-i <image> | -l <imagelink>] [-o <output>] [--tags <tags>...] [[-p <points> -c <comments>] | -C <Ctext>]

Options:
    -h --help                               Show this help message.
    -v --version                            Show the current version.
    -T <title>, --title <title>             Specify the meme title.
    -t <text>, --text <text>                Specify the text below the title and above the image.
    -i <image>, --image <image>             Specify the relative or absolute path to your image.
    -o <output>, --out <output>             The output file [default: ./aboveMeme.png]
    --tags <tags>                           As many or few tags as you want.
    -p <points>, --points <points>          How many points you want. Don't specify if you want me to not display any.
    -c <comments>, --comments <comments>    How many comments there are below your post. Don't specify if you want mo to not display any.
    -C <Ctext>                              Alternatively to -c and/or -p, specify the complete text to be displayed in the light-grey font.
    -l <imagelink>, --link <imagelink>        Alternatively to -i you can provide the image per link

"""
from docopt import docopt                   # parsing
from sanitizer import Sanitizer # sanitizing html

VERSION = 0.1

def main(arguments):
    print("You have called main with arguments = \n{0}".format(arguments))
    if(arguments['--link']):
        mySanitizer = Sanitizer()
        print(mySanitizer.cleanHTML("some test <script>alert('123');</script> input")) # TODO: write actual logic

if __name__ == '__main__':
    arguments = docopt(__doc__, version="MakeAboveMeme {0}".format(VERSION))
    main(arguments)
