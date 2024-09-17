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
		tokens = re.findall(r'[\w]+', f.read())
		tokens = [token.lower() for token in tokens ]
		corpus[path] = Counter(tokens)
	return corpus

def tfidf(query, corpus):
	query = re.findall(r'[\w]+', query)
	query = [q.lower() for q in query]
	#print(query)

	occur = {}

	for file in corpus.keys():
		for term in query:
			if term in corpus[file]:
				occur[file] = corpus[file][term]
	print(occur)


def main():
	textdir = './text-files'
	corpus = tokenize(textdir)
	'''
	for k in corpus.keys():
		print(k,corpus[k])
		break
		'''
	tfidf("e", corpus)

if __name__ == "__main__":
	main()
