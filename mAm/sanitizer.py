import lxml # code and imports inspired by https://stackoverflow.com/a/8554251/2550406
from lxml.html.clean import Cleaner

class Sanitizer:
    """Used to get rid of potentially evil code in strings and images."""
    def __init__(self):
        self._cleaner = Cleaner()

    # removes javascript and styles, but keeps everything else intact
    # python2 doesn't yet feature explicit typing....
    # cleanHTML => self -> str --> str
    def cleanHTML(self, toClean):
        # see http://lxml.de/api/lxml.html.clean.Cleaner-class.html for all options
        self._cleaner.javascript = True # Filter javascript
        self._cleaner.style = True # Filter styles and stylesheets
        self._cleaner.embedded = True # Disallow flash, iframes
        if not __debug__: # if the -O flag for debugging was set (confusing, I know)
            print("cleanHTML  >>  Input String:")
            print(toClean)
            print("cleanHTML  >>  With Javascript & Styles:")
            print(lxml.html.tostring(lxml.html.fragment_fromstring(toClean, create_parent='div')))
            print("cleanHTML  >>  Without Javascript & Styles:")
            print(lxml.html.tostring(self._cleaner.clean_html(lxml.html.fragment_fromstring(toClean, create_parent='div'))))
        
        print("cleanHTML  >>  finished.")


if __name__ == '__main__':
    mySanitizer = Sanitizer()
    mySanitizer.cleanHTML(" href='test'> this is a debug string</a>")
