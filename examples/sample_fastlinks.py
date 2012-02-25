from fastlinks import getLinks

__author__ = 'Lukas Salkauskas'

def main():

    # If you like you can provide any html content here.

    content = """
    <LINK REL="SHORTCUT ICON" HREF="favicon.ico" />

    		src='/clickme.php?id=10&amp;stats=23d'

    		URL="http://www.testsite.com/verygood.html"

    href='www.testsite.com/hello placentas/word.htm'
    href='../test.html'
        """

    links = getLinks(content, 'http://www.testsite.com/heelo/planet')
    for i in range(0, len(links)):
        print '[' + str(i + 1) + '] ' + links[i]

if __name__ == '__main__':
    main()
