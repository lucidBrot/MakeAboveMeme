import lxml # code and imports inspired by https://stackoverflow.com/a/8554251/2550406
from lxml.html.clean import Cleaner

class Sanitizer:
    """Used to get rid of potentially evil code in strings and images."""
    def __init__(self):
        self._cleaner = Cleaner()

    def cleanHTML(self):
        self._cleaner.javascript = True # Filter javascript
        self._cleaner.style = True # Filter styles and stylesheets
        if not __debug__: # if the -O flag for debugging was set (confusing, I know)
            print("cleanHTML  >>  With Javascript & Styles:")
            print(lxml.html.tostring(lxml.html.parse('../somepost.html'))) # TODO: use the actual arguments
            print("cleanHTML  >>  Without Javascript & Styles:")
            print(lxml.html.tostring(self._cleaner.clean_html(lxml.html.parse('../somepost.html'))))
        
        print("cleanHTML  >>  finished.")

if __name__ == '__main__':
    mySanitizer = Sanitizer()
    mySanitizer.cleanHTML()
