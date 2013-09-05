def biggest(aDict):
	'''
	aDict: A dictionary, where all the values are lists.

	returns: The key with the largest number of values associated with it
	'''
	# Your Code Here
	ab_max = [0,0]
	curr_max = [0,0]
	for key,value in aDict.items():
		print key
		print value
		curr_max[1] = len(value)
		curr_max[0] = key
		if ab_max[0] == 0:
			ab_max[0] = key
			ab_max[1] = len(value)
		if curr_max[1] > ab_max[1]:
			ab_max[0] = curr_max[0]
			ab_max[1] = curr_max[1]
	if ab_max[0] == 0:
		ab_max[0] = 'None'
	return ab_max[0]
	
print biggest({})
#print biggest({'i': []})
#print biggest({'a': [9, 10, 17, 17], 'c': [20, 12, 3, 20, 16, 11, 20], 'b': [14, 19]})
#print biggest({'a': [18, 16, 17, 11, 12], 'b': [4, 4, 18, 18, 20, 9, 7, 10]})