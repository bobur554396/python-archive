import pprint
import sqlite3 as sql
import sys, subprocess
from os import listdir
from cStringIO import StringIO

from os.path import isfile, join

import operator

con = sql.connect('books.db')
cur = con.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, content text)')

def store_in_db():
    mypath = ("/Users/terences/PycharmProjects/sandbox/scrapy")
    # mypath = ("/Users/terences/Downloads/abooks")

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    pdfs = [f for f in onlyfiles if f.endswith(".pdf")]
    con = None

    # This grabs book data
    try:

        for f in pdfs:
            text = None
            tmp = StringIO()
            output = subprocess.Popen(["java", "-jar", "pdfbox-app-2.0.2.jar", "ExtractText","-encoding", "UTF-8", "-console", "%s/%s" % (mypath, f)], stdout=subprocess.PIPE).communicate()[0]
            #todo: split by pages
            #print output
            text = output
            title = f.replace(" ", "_").replace(".pdf", "")
            print title
            cur.execute('INSERT INTO books(name, content) VALUES ("%s", "%s")' % (title, str(text)))

        cur.execute('SELECT id, name, content FROM books')
        data = cur.fetchall()

        pprint.pprint(data)

    except sql.Error, e:
        print "Error %s: " % e.args[0]
        sys.exit(1)

    # finally:
    #     if con:
    #         con.close()

store_in_db()
cur.execute('SELECT name, content FROM books')
data = cur.fetchall()


def extract_knowledge(title, text_study):
    from nltk import PunktWordTokenizer
    from nltk.corpus import stopwords
    stop = set(stopwords.words('english'))
    pwt = PunktWordTokenizer()
    tokens = pwt.tokenize(text_study)
    tokens = [i for i in tokens if i.lower() not in stop]
    hist = {}
    for token in tokens:
        if len(token) == 1:
            continue
        if token.lower() in hist:
            hist[token.lower()] += 1
        else:
            hist[token.lower()] = 1
    # now that word freqs are received, find n-best
    sorted_hist = sorted(hist.items(), key=operator.itemgetter(1), reverse=True)

    for i in sorted_hist:
        print i

for book in data:
    print book[0]
    print book[1]
    title = book[0]
    text_study = book[1]
    extract_knowledge(title, text_study)
