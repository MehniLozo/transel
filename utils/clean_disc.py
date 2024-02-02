from pickle import load 
from pickle import dump 
from collections import Counter 

def clean_sents_open(name):
    return load(open(name,'rb'))

def clean_sents_save(sents, name):
    dump(sents,open(name,'wb'))
    print("------------ SAVING %s ------------" % name)

def freq(cts): # lines contents for frequency table creation
    v = Counter()
    for l in cts:
        tks = l.split()
        v.update(tks)
    return v

def trimming(vocab, min_occ): 
    # reducing table size from all non frequent words
    tks = [k for k, o in vocab.items() if o >= min_occ]
    return set(tks)

def update(cts,vocab): ## updating lines containing OOV -> UNK
    new_ls = list()  
    for l in cts:
        new_tks = list()
        for tk in l.split():
            if tk in vocab:
                new_tks.append(tk)
            else:
                new_tks.append('unk')
        new_l = ' '.join(new_tks)
        new_ls.append(new_l)
    return new_ls
    