# import BeautifulSoup
# import urllib
# r = urllib.urlopen('http://it-ebooks.directory/categories.html').read()
# bs = BeautifulSoup(r)
#
# print type(bs)

from bs4 import BeautifulSoup
import urllib
import subprocess
PATH = 'http://www.allitebooks.com/'
def write_to_txt(self, PATH=""):
    r = urllib.urlopen(PATH).read()
    soup = BeautifulSoup(r, "html.parser")
    # print soup.prettify()

    books = soup.find_all("a", rel="bookmark")


    page = PATH + "page/"


    for i in range(2, 624):
        url = page + str(i) + "/"
        r = urllib.urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        # print soup.prettify()
        temp_list = soup.find_all("a", rel="bookmark")
        print i
        books += temp_list
    f = open("/Users/terences/PycharmProjects/sandbox/book-url-list.txt", "w+")
    s = ""
    for book in books:
        # print book
        s += str(book) + '\n'
    f.write(s)


def download_books(self):
    with open(LIST) as f:
        # print f.read()
        urlMap = {}
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.replace("\"", "")
            r = urllib.urlopen(line).read()
            soup = BeautifulSoup(r, "html.parser")
            # print soup.prettify()
            temp_list = soup.find_all("a", target="_blank")
            urlMap[temp_list[0]["href"]] = ""
    list = urlMap.keys()
    print "Copying Successfully...."
    for i in list:
        subprocess.call(["wget", "-O","/Users/terences/PycharmProjects/sandbox/books/"+str(i).split("/")[len(str(i).split("/")) - 1],i])

LIST = "/Users/terences/PycharmProjects/sandbox/book-url-list.txt"
# write_to_txt(PATH)
download_books(LIST)