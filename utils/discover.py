import pickle
from pickle import dump

def load(name):
    file = open(name, mode='rt', encoding='utf-8')
    text = file.read()
    file.close()
    return text
def trans_sent(doc):
    return doc.strip().split('\n')
