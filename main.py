#! /usr/bin/env python3

from math import log10
from os import listdir
from os.path import isfile, join
from collections import Counter
import re

def tokenize(textdir):
        paths = [f for f in listdir(textdir) if isfile(join(textdir, f))]
        corpus = {}
        for path in paths:
                f = open(join(textdir, path))
                tokens = re.findall(r'[\w]+', f.read())
                tokens = [token.lower() for token in tokens ]
                corpus[path] = Counter(tokens)
        return corpus

def tf(target, tokens):
        return {k:log10(1 + tokens[k][target]) for k in tokens.keys()}

def idf(target, tokens):
        total = len(list(tokens.keys()))+1
        occ = 1.0
        for k,v in tokens.items():
                if target in v:
                    occ+=1
        return log10(float(total)/occ)

def tfidf(target, tokens):
        ret = {}
        idfs = idf(target, tokens)
        tfs = tf(target, tokens)
        for k,v in tfs.items():
                ret[k] = v*idfs
        return ret

def main():
        textdir = './text-files'
        targets = ["noble", "is"]
        files_2_tokens = tokenize(textdir)
        for target in targets:
                tfidfs = tfidf(target, files_2_tokens)
                print("{}: {}".format(target, tfidfs))
                print()

if __name__ == "__main__":
        main()
