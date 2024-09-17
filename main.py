#! /usr/bin/env python3

from os import listdir
from os.path import isfile, join
from collections import Counter
import re

def tokenize(textdir):
	paths = [f for f in listdir(textdir) if isfile(join(textdir, f))]
	corpus = {}
	for path in paths:
		f = open(join(textdir, path))
		tokens = re.findall(r'[a-zA-Z0-9]', f.read())
		tokens = [token.lower() for token in tokens ]
		corpus[path] = Counter(tokens)
	return corpus

def tfidf(term, corpus):
	term_tokens = re.findall(r'[a-zA-Z0-9]', term)
	for file in corpus.keys():




def main():
	textdir = './text-files'
	corpus = tokenize(textdir)
	'''
	for k, v in tokens.items():
		print("{} -> {}".format(k, v))
	#print(tokens)
	'''
	tfidf("murders", corpus)

if __name__ == "__main__":
	main()
