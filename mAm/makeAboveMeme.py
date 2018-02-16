#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MakeAboveMeme

Usage:
    makeAboveMeme.py (-h | -v)
    makeAboveMeme.py [-T <title>] [-t <text>] [-i <image>] [-o <output>] [--tag <tag> ...] [[-p <points> -c <comments>] | -C <Ctext>] [-X]

Options:
    -h --help                               Show this help message.
    -v --version                            Show the current version.
    -T <title>, --title <title>             Specify the meme title.
    -t <text>, --text <text>                Specify the text below the title and above the image.
    -i <image>, --image <image>             Specify the relative or absolute path to your image.
    -o <output>, --out <output>             The output file [default: ./aboveMeme.png]
    --tag <tag>                             Repeat '--tag mytag' as often as you want. You need to type the '--tag' every time.
    -p <points>, --points <points>          How many points you want. Don't specify if you want me to not display any.
    -c <comments>, --comments <comments>    How many comments there are below your post. Don't specify if you want mo to not display any.
    -C <Ctext>                              Alternatively to -c and/or -p, specify the complete text to be displayed in the light-grey font.
    -X                                      Use the already running X-server instead of xvfb

"""
from docopt import docopt                   # parsing
from sanitizer import Sanitizer             # sanitizing html
import os                                   # for script file path
from string import Template                 # for text substitution
import subprocess                           # for running webkit2png
import tempfile                             # for creating temporary files

VERSION = "0.5.4"
MAM_TEMPLATE_FILENAME = 'mam.html' # css is included from there. currently from mam.css
TAG_HTML_TEMPLATE_STRING = Template('<a href="" class="A">${tagtext}</a> ')
COMMENTLINE_TEMPLATE_STRING = Template('<a href="" class="C">${points}</a> · <a href="" class="C">${comments}</a>')
TXT_TEMPLATE_STRING = Template('<div class="TXT">${text}</div>')

def main(arguments):
    # initialize some globals
    global script_dir_g, MAM_TEMPLATE_FILENAME, template_path_g, output_path_g
    script_dir_g = os.path.dirname(__file__)
    template_path_g = os.path.join(script_dir_g, MAM_TEMPLATE_FILENAME)

    print("You have called main with arguments = \n{0}".format(arguments))

    output_path_g = arguments['--out'] # should always exist because of default value specified in help message

    makeAbove(arguments)
    print("done")  

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
    # clean title
    title = mySanitizer.cleanHTML(title)

    image="" 
    if arguments['--image'] is not None:
        image=arguments['--image']
    image = mySanitizer.cleanHTML(image)

    # create all tags and store them in one long string
    global TAG_HTML_TEMPLATE_STRING
    alltags=""
    for tag in arguments['--tag']:
        alltags+= TAG_HTML_TEMPLATE_STRING.substitute({'tagtext':mySanitizer.cleanHTML(tag)})

    # for the line with points and comments
    global COMMENTLINE_TEMPLATE_STRING
    if arguments['-C'] is not None:
        argsC = mySanitizer.cleanHTML(arguments['-C'])
        commentline = '<a href="" class="C">{0}</a>'.format(argsC)
    elif (arguments['--comments'] is None) and (arguments['--points'] is None):
        commentline = ""
    else:
        comments = 0 if arguments['--comments'] is None else arguments['--comments']
        points = 0   if arguments['--points'] is None else arguments['--points']
        comments = mySanitizer.cleanHTML(comments)
        points = mySanitizer.cleanHTML(points)
        subC = "{0} comments".format(comments)
        subP = "{0} points".format(points)
        commentline = COMMENTLINE_TEMPLATE_STRING.substitute({'points':subP, 'comments':subC})

    # set text if there should be
    global TXT_TEMPLATE_STRING
    text = ''
    if arguments['--text'] is not None:
        text=arguments['--text']
        text = mySanitizer.cleanHTML(text)
        text = TXT_TEMPLATE_STRING.substitute({'text':text}) # write text into html-string

    substDir = { 'title':title, 'image':image, 'tags':alltags, 'commentline':commentline, 'text':text }
    tempStr = template.substitute(substDir)

    # write result to temp file
    (fd, filename) = tempfile.mkstemp(suffix='.html', dir=script_dir_g) # create the tempfile in the script-containing directory
    try:
        tfile = os.fdopen(fd, "w") 
        tfile.write(tempStr)
        tfile.close()
        if not arguments['-X']:
            webkitres = subprocess.check_output(["webkit2png", filename, "-o", output_path_g, "-x", "70", "1000"])
        else:
            webkitres = subprocess.check_output(["webkit2png", filename, "-o", output_path_g])
        print("Called webkit2png with filename {0} and output path {1}".format(filename, output_path_g))
    except subprocess.CalledProcessError as e:
        print("webkit2png failed. DO SOMETHING.") # handle error of webkit2png? I don't know how, so not my job
        exit(2)
    finally:
        os.remove(filename)

# for other files to call the script
def call():
    arguments = docopt(__doc__, version="MakeAboveMeme {0}".format(VERSION))
    main(arguments)

if __name__ == '__main__':
    arguments = docopt(__doc__, version="MakeAboveMeme {0}".format(VERSION))
    main(arguments)
