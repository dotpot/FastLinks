import re, urlparse, posixpath
__author__ = 'Lukas Salkauskas'

_linksPattern = re.compile(r'(?:href|src|url)=[\'"]?([^\'">]+)')

def normalize(base,url):
    join = urlparse.urljoin(base, url)
    url = urlparse.urlparse(join)
    path = posixpath.normpath(url[2])
    return urlparse.urlunparse((url.scheme, url.netloc, path, url.params, url.query, url.fragment))

def getLinks(content, url):
    """
    Possible todo:
     - Integrate extraction of link text.
     - Integrate extraction of links from plane text.
     - Rethink specific cases part.
     - F*ck, what else...:)
    """

    hostname = urlparse.urlparse(url).hostname + '/'
    content = content.lower()
    links = re.findall(_linksPattern, content)
    
    for i in range(0, len(links)):
        links[i] = links[i].replace('&amp;', '&')
        if not links[i].startswith('http://'):
            if links[i].find('..') != -1:
                links[i] = normalize(url, links[i])

            if links[i].find(hostname) == -1:
                links[i] = hostname + links[i]

            links[i] = links[i].replace('//', '/')
            links[i] = 'http://' + links[i]

        # Specific cases  ( maybe there is much more easier way of doing this? )       
        if links[i].find('//', 7) != -1 or links[i].count('http:') > 1:
            links[i] = links[i].replace('http:', '')
            links[i] = links[i].replace('//', '')
            links[i] = 'http://' + links[i]
            links[i] = links[i].replace('///', '//')

        if links[i].find('\/') != -1:
            linsk[i] = links[i].replace('\/', '/')

    return list(set(links))