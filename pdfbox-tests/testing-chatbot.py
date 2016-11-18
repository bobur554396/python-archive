import os
import subprocess

# This grabs book data
# subprocess.call(["java","-jar", "pdfbox-app-2.0.2.jar",
#                  "ExtractText", "/Users/terences/Downloads/approximate_injectivity.pdf",
#                  "output/approximate_injectivity.txt"])
import nltk
# nltk.download()

text_file = ""
with open("output/MLfH.txt") as f:
    text_file = f.read()

text_file = text_file.decode('utf-8').strip()
# splits sentences
from nltk.tokenize import sent_tokenize
tokens = sent_tokenize(text_file)
# print tokens

# splits words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text_file)
# print tokens

# whitespace tokenizer
from nltk.tokenize import regexp_tokenize
tokenizer = regexp_tokenize(text_file,'\s+', gaps=True)
# print tokenizer

from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
words = tokenizer
# print [word for word in words if word not in english_stops]

#look up words and print synset
from nltk.corpus import wordnet
syn = wordnet.synsets('cookbook')[0]
print syn.name()
print syn.definition()
print syn.hypernyms()
print syn.hypernyms()[0].hyponyms()
print syn.root_hypernyms()
print syn.hypernym_paths()



#
# for w in words:
#     print w
#     syn = wordnet.synsets(w)
#     if (type(syn) == 'list'):
#         syn = syn[0]
#     # print syn
#     if (len(syn) != 0):
#         for i in syn:
#             # print i
#             # print '\t[', i.name(),']'
#             print '\t--', i.definition()



from nltk.tag import UnigramTagger
from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:3000]
tagger = UnigramTagger(train_sents)
print tagger.tag(treebank.sents()[0])
