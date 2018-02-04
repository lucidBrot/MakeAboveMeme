import cgi

class Sanitizer:
    """Used to get rid of potentially evil code in strings and images."""
    def cleanHTML(self, toClean):
        # allow newlines with <br> and \n as well as the actual newline character
        return cgi.escape(toClean.replace("\\n", "\n").replace("<br>","\n")).replace("\n","<br>")

if __name__ == '__main__':
    mySanitizer = Sanitizer()
    print(mySanitizer.cleanHTML('<img src="https://img-9gag-fun.9cache.com/photo/aYgwO3m_700b.jpg" alt="When you love Earth-chan" id="IMG_15" />'))
