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

def termfreq(target, tokens):
	tfs = {}
	for k in tokens.keys():
		count = 0
		for c in tokens[k].values():
			count += c
		tf = float(tokens[k][target])/float(count)
		tfs[k] = tf
	return tfs

def main():
	textdir = './text-files'
	target1 = "noble"
	target2 = "is"
	files_2_tokens = tokenize(textdir)
	freqs1 = termfreq(target1, files_2_tokens)
	freqs2 = termfreq(target2, files_2_tokens)
	print("{}: {}".format(target1, freqs1))
	print()
	print("{}: {}".format(target2, freqs2))

if __name__ == "__main__":
	main()
