# Dev-sprint4: ThinkPython
# Ceceilia Allwein 


# Exercise 12.4 - anagrams

'''

1
Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams.

Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']

Hint: you might want to build a dictionary that maps from a set of letters to a list of words that can be spelled with those letters. The question is, how can you represent the set of letters in a way that can be used as a key?
'''

def read_file(filename): 
	storage = dict()
	with open(filename) as fin: 
		for line in fin: 
			line = line.strip()
			storage[line] = storage.get(line,0) + 1
		return storage

print read_file('words.txt')



