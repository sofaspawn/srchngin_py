#! /usr/bin/env python3

from os import listdir
from os.path import isfile, join
from collections import Counter
import re

def tokenize(textdir):
	paths = [f for f in listdir(textdir) if isfile(join(textdir, f))]
	corpus = []
	for path in paths:
		f = open(join(textdir, path))
		tokens = re.findall(r'[a-zA-Z0-9.,!?@#$%^&*()_+\-=\[\]{}<>/\\|`~\'"]', f.read())
		tokens = [token.lower() for token in tokens ]
		corpus.append(Counter(tokens))
	return corpus

def main():
	textdir = './text-files'
	tokens = tokenize(textdir)
	print(tokens[0])


if __name__ == "__main__":
	main()
