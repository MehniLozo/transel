from pickle import load 
from pickle import dump 
from collections import Counter 

def clean_sents_open(name):
    return load(open(name,'rb'))

def clean_sents_save(sents, name):
    dump(sents,open(name,'wb'))
    print("------------ SAVING %s ------------" % name)

def freq(contents): # lines contents for frequency table creation
    v = Counter()
    for l in contents:
        tks = l.split()
        v.update(tks)
    return v

def trimming(vocab, min_occ): 
    # reducing table size from all non frequent words
    tks = [k for k, o in vocab.items() if o >= min_occ]
    return set(tks)
