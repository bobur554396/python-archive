import sys, os, bs4 as bs, urllib2, pprint


with open("/Users/terences/PycharmProjects/sandbox/book-url-list.txt", "r") as f:
    lines = f.readlines()
f = open("/Users/terences/PycharmProjects/sandbox/book-url-list2.txt", "w")
def chunks(l,n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
url_chunks = list(chunks(lines, 200))
    # // *[ @ id = "main-content"] / div / article / footer / div / span[1].download-links / a["href"]
uniq_links = {}
i = 0
for chunk in url_chunks:
    print "grabbing new chunk"
    # i += 1
    for line in chunk:
        # print i
        # i += 1
        page = urllib2.urlopen(line).read()
        html = page
        soup = bs.BeautifulSoup(html, 'html.parser')
        links = soup.find_all("span", class_="download-links")
        uniq_links[links[0].a["href"]] = line
    pdf_urls = uniq_links.keys()
    for i in pdf_urls:
        f.write(i + '\n')
    uniq_links.clear()

f.close()