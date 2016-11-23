import urllib2

# def download(url):
#     return urllib2.urlopen(url).read()
import re
import urlparse

#todo: add download_with_agent_and_proxy to all calls

def download(url):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
    return html

def download_retry(url, num_retries=2):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP erros
                return download(url, num_retries - 1)
    return html

def download_with_agent(url, user_agent='wswp', num_retries=2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP erros
                return download(url, num_retries - 1)
    return html

def download_with_agent_and_proxy(url, user_agent='wswp', proxy=None, num_retries=2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        # html = urllib2.urlopen(request).read()
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP erros
                return download(url, num_retries-1)
    return html
def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)
        print html

print download('http://example.webscraping.com/robots.txt')

import itertools
def retry_steps():
    # maximum number of consecutive download errors allowed
    max_errors = 5
    # current number of consecutive download errors
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' % page
        html = download(url)
        if html is None:
            # received an error trying to download this webpage
            num_errors += 1
        if num_errors == max_errors:
            # reached maximum number of
            # consecutive errors so exit
            break
        else:
            # success - can scrape the result
            # ...
            num_errors = 0


def link_crawler(seed_url, link_regex):
    """
    Crawl from the given seed URL following links matched by link_regex
    :param seed_url:
    :param link_regex:
    :return:
    """
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

def get_links(html):
    """Return a list of links from html
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)
