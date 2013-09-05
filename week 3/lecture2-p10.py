def howMany(aDict):
	'''
	aDict: A dictionary, where all the values are lists.

	returns: int, how many values are in the dictionary.
	'''
	# Your Code Here
	count = 0
	for x,y in aDict:
		count += len(y)
	return count;