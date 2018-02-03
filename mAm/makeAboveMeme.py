#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from sanitizer import Sanitizer             # sanitizing html
import os                                   # for script file path
from string import Template                 # for text substitution
import subprocess                           # for running webkit2png
import tempfile                             # for creating temporary files

VERSION = 0.1
MAM_TEMPLATE_FILENAME = 'mam.html'

def main(arguments):
    # initialize some globals
    global script_dir_g, MAM_TEMPLATE_FILENAME, template_path_g, output_path_g
    script_dir_g = os.path.dirname(__file__)
    template_path_g = os.path.join(script_dir_g, MAM_TEMPLATE_FILENAME)

    print("You have called main with arguments = \n{0}".format(arguments))

    output_path_g = arguments['--out'] # should always exist because of default value specified in help message

    makeAbove(arguments)
    print("done") # TODO: write actual logic

# arguments is a list of arguments, as provided by docopt
def makeAbove(arguments):
    global template_path_g, output_path_g, script_dir_g

    mySanitizer = Sanitizer() # default sanitizer for mAm. Clears JS and CSS, leaves html in.
    # for every argument, check if set and handle accordingly

    with open(template_path_g, 'r') as templateFile:
        template = Template(templateFile.read())
    
    # set title if there should be one
    if arguments['--title'] is not None:
        title = arguments['--title']
    else:
        title = ""

    image="http://i0.kym-cdn.com/photos/images/original/001/330/335/b84.png"
    if arguments['--image'] is not None:
        image=arguments['--image']

    substDir = { 'title':title, 'image':image }
    tempStr = template.substitute(substDir)

    # write result to temp file
    (fd, filename) = tempfile.mkstemp(suffix='.html', dir=script_dir_g) # create the tempfile in the script-containing directory
    try:
        tfile = os.fdopen(fd, "w")
        tfile.write(tempStr)
        tfile.close()
        webkitres = subprocess.check_output(["webkit2png", filename, "-o", output_path_g, "-x", "70", "1000"])
        print("Called webkit2png with filename {0} and output path {1}".format(filename, output_path_g))
    except subprocess.CalledProcessError as e:
        print("webkit2png failed. DO SOMETHING.") # TODO: handle error of webkit2png
    finally:
        os.remove(filename)

if __name__ == '__main__':
    arguments = docopt(__doc__, version="MakeAboveMeme {0}".format(VERSION))
    main(arguments)
