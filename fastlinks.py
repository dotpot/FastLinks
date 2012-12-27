import re, urlparse, posixpath

__author__ = 'dotpot'

_linksPattern = re.compile(r'(?:href|src|url)=[\'"]?([^\'">]+)')


def normalize(base,url):
    join = urlparse.urljoin(base, url)
    url = urlparse.urlparse(join)
    path = posixpath.normpath(url[2])
    return urlparse.urlunparse((url.scheme, url.netloc, path, url.params, url.query, url.fragment))


def get_links(content, url):
    """
    Possible todo:
     - Integrate extraction of link text.
     - Integrate extraction of links from plane text.
     - Rethink specific cases part.
     - F*ck, what else...:)
    """
    if content is None or url is None:
        return None

    hostname = urlparse.urlparse(url).hostname + '/'
    content = content.lower()
    links = re.findall(_linksPattern, content)
    
    for i, link in enumerate(links):
        link = link.replace('&amp;', '&')
        if not link.startswith('http://') and not link.startswith('https://'):
            if link.find('..') != -1:
                link = normalize(url, link)

            if link.find(hostname) == -1:
                link = hostname + link

            link = link.replace('//', '/')
            link = 'http://' + link

        # Specific cases ( maybe there is much more easier way of doing this? )
        if link.find('//', 7) != -1 or link.count('http:') > 1:
            link = link.replace('http:', '')
            link = link.replace('//', '')
            link = 'http://' + link
            link = link.replace('///', '//')

        if link.find('\/') != -1:
            link = link.replace('\/', '/')
        links[i] = link
    # return duplicates free list of links
    return list(set(links))
