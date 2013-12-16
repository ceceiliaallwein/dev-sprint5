# Dev-sprint4: ThinkPython
# Ceceilia Allwein 


# Exercise 12.4 - anagrams



def sort_string(string):
    '''Creates a sorted string.'''
    return ''.join(sorted(string))


def read_file(filename): 
	'''Reads a given text file and creates 
	a dictionary of sorted strings and their 
	anagrams.

	keys = sorted string
	value = list of anagrams 

	'''
	storage = {}
	with open(filename) as fin: 
		for line in fin: 
			# removes formatting, incl. trailing spaces and linebreaks
			line = line.strip().lower()
			# determines if the sorted string is a unique key
			if sort_string(line) not in storage.keys(): 
				# initializes a value list with a singleton
				storage[sort_list(line)] = [line]
			else: 
				# appends an anagram to the value list
				storage[sort_string(line)].append(line)
		return storage

# result = read_file('words.txt')


def anagrams(word,filename):
	'''Reads a given text file and returns
	anagrams for a given word.

	key = given string
	value = list of anagrams 
	'''
	# converts given word to a sorted string
	x = sort_string(word).lower()
	# initializes an empty list to store anagrams
	l = []
	with open(filename) as fin: 
		for line in fin: 
			# removes formatting, incl. trailing spaces + line breaks
			line = line.strip().lower()
			# converts line in text file to a sorted string
			y = sort_string(line)
			# determines if given word and line in text file match
			if x == y: 
				# appends matched string (not sorted string!) to list of anagrams
				l.append(line)
		return word,l 

print anagrams('theist','words.txt')



def search(word,anagram_dict): 
	x = sorted(word)
	x = ''.join(x)
	return anagram_dict[x]


# def match(filename): 
	







