from unittest import TestCase
from fastlinks import *

__author__ = 'Lukas Salkauskas'

class TestFastLinks(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getLinks(self):
        # Provide sample content
        content = """
        <LINK REL="SHORTCUT ICON" HREF="favicon.ico" />

        		src='/clickme.php?id=10&amp;stats=23d'

        		URL="http://www.testsite.com/verygood.html"

        href='www.testsite.com/hello placentas/word.htm'
        href='../test.html'
        """

        links = getLinks(content, 'http://www.testsite.com')

        # Check count of links.
        self.assertEqual(5, len(links))

        # Check content of the result.
        listOfExpected = \
        [
            'http://www.testsite.com/favicon.ico',
            'http://www.testsite.com/clickme.php?id=10&stats=23d',
            'http://www.testsite.com/verygood.html',
            'http://www.testsite.com/hello placentas/word.htm',
            'http://www.testsite.com/test.html'
        ]

        expectedResult = True
        for actual in links:
            if actual not in listOfExpected:
                expectedResult = False

        self.assertEqual(True, expectedResult)
    def test_normalize(self):
        actual = ''
        expected = ''

        # Check different scenarios.

        actual = normalize('http://test.com/', '/path/../path/.././path/./')
        expected = 'http://test.com/path'
        self.assertEquals(actual, expected)

        actual = normalize('http://test.com/path/x.html', '/path/../path/.././path/./y.html')
        expected = 'http://test.com/path/y.html'
        self.assertEquals(actual, expected)

        actual = normalize('http://test.com/', '../../../../path/')
        expected = 'http://test.com/path'
        self.assertEquals(actual, expected)

        actual = normalize('http://test.com/x/x.html', '../../../../path/foobar.html')
        expected = 'http://test.com/path/foobar.html'
        self.assertEquals(actual, expected)

        actual = normalize('http://test.com/4/z.html', '1/2/3/foo.html')
        expected = 'http://test.com/4/1/2/3/foo.html'
        self.assertEquals(actual, expected)

        actual = normalize('http://test.com/4/x.html', '../1/2/3/foo.html')
        expected = 'http://test.com/1/2/3/foo.html'
        self.assertEquals(actual, expected)
