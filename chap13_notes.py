# Chapter 13 notes

import string

def process_file(filename):
	histogram = dict()
	with open(filename) as fin: 
		for line in fin: 
			process_line(line,histogram)
		return histogram

def process_line(line,histogram):
	line = line.replace('-',' ')

	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()

		histogram[word] = histogram.get(word,0) + 1

def total_words(histogram): 
	return sum(histogram.values())

def different_words(histogram):
	return len(histogram)

h = process_file('emma.txt')
t = total_words(h)
print h
print t
