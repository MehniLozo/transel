import pickle
from pickle import dump
import re 
import string 
import unicodedata

def load(name):
    file = open(name, mode='rt', encoding='utf-8')
    text = file.read()
    file.close()
    return text
def trans_sent(doc):
    return doc.strip().split('\n')

def len_sent(sentences):
    l = [len(s.split()) for s in sentences]
    return min(l), max(l)

def lclean(lines):
    res = list()
    re_print = re.compile('[^%s]' % re.escape(string.printable))
    t = str.maketrans('','',string.punctuation)
    for l in lines:
        l = unicodedata.normalize('NFD',l).encode('ascii','ignore')
        l = l.decode('UTF-8')
        l = l.split()
        # lowercasing words
        l = [w.lower() for w in l]
        l = [w.translate(t) for w in l] # for punctuations
        l = [re_print.sub('',w) for w in l] # for non-printables
        l = [w for w in l if w.isalpha()] # has number in it ???
        res.append(''.join(l)) ## appending line
    return res