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
        # return {k:log10(1 + tokens[k][target]) for k in tokens.keys()}
        ret = {}
        for f,c in tokens.items():
                total = float(sum(c.values()))
                count = float(c[target])
                ret[f] = count/total
        return ret

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

def handleinput(s):
        # maybe use some kind of combination of both these things
        # should i search by word or by characters? idk
        return re.findall(r'[\w]+', s)
        # return re.findall(r'[a-zA-Z]', s)

def main():
        textdir = './text-files'
        search_term = input(">")
        targets = handleinput(search_term)
        files_2_tokens = tokenize(textdir)
        final = {}
        for target in targets:
                tfidfs = tfidf(target, files_2_tokens)
                for k,v in tfidfs.items():
                        if k in final:
                                final[k]+=v
                        else:
                                final[k]=v
        final = sorted(final, key=final.get, reverse=True)
        print(final)

if __name__ == "__main__":
        main()
