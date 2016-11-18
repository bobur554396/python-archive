import csv

import itertools

import nltk
from operator import itemgetter as _itemgetter
import heapq as _heapq

vocabulary_size = 8000
unknown_token = "UNKNOWN_TOKEN"
sentence_start_token = "SENTENCE_START"
sentence_end_token = "SENTENCE_END"
# todo: had to write this because FreqDist.most_common() no longer works
# def most_common(self, fd=None, n=None):
#     if fd is None:
#         return None
#     if n is None:
#         return sorted(fd.iteritems(), key=_itemgetter(1), reverse=True)
#     return _heapq.nlargest(n, fd.iteritems(), key=_itemgetter(1))

print( "Reading CSV file...")
with open("/Users/terences/Downloads/rnn-tutorial-rnnlm-master/data/reddit-comments-2015-08.csv", 'rb') as f:
    reader = csv.reader(f, skipinitialspace=True)
    reader.next()
    # Split full comments into sentences
    sentences = itertools.chain(*[nltk.sent_tokenize(x[0].decode('utf-8').lower()) for x in reader])
    sentences = ["%s %s %s" % (sentence_start_token, x, sentence_end_token) for x in sentences]
print "Parsed %d sentences." % (len(sentences))

tokenize_sentences = [nltk.word_tokenize(sent) for sent in sentences]

word_freq = nltk.FreqDist(itertools.chain(*tokenize_sentences))
print("Found %d unique words tokens." % len(word_freq.items()))

# vocab = word_freq.most_common(vocabulary_size - 1)
vocab = word_freq.most_common(word_freq, vocabulary_size - 1)
index_to_word = [x[0] for x in vocab]
index_to_word.append(unknown_token)
word_to_index = dict([(w,i) for i,w in enumerate(index_to_word)])

print "Using vocabulary size %d." % vocabulary_size
print "The least frequent word in our vocabulary is '%s' and appeared %d times." % (vocab[-1][0], vocab[-1][1])
