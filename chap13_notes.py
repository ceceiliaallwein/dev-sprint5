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

# h = process_file('emma.txt')
# t = total_words(h)
# print 'Total number of words: ' + str(len(h))
# print 'Number of different words: ' + str(t)


def most_common(histogram):
	t = []
	for key, value in hist.items():
		t.append((value,key))

	t.sort(reverse=True)
	return t



#Exercise 13.5

def histogram(s): 
	d = dict()
	for c in s: 
		if c not in d: 
			d[c] = 1
		else: 
			d[c] += 1
	return d 


def print_hist(h): 
	output = dict()
	for c in h:
		print c, h[c]

import random
print histogram('ceceilia')

def choose_rand(arg):
	d = histogram(arg)
	return random.choice(list(d.keys()))
	
def choose_weighted(arg):
	'''Returns a random value from a 
	given histogram. Weighted by the 
	number of times it appears.'''
	d = histogram(arg)

# http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice?lq=1


print choose('ceceilia')




# h = histogram('ceceilia')
# print h.get('a',0)
# print_hist(h)




