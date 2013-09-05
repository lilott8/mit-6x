def oddTuples(aTup):
	'''
	aTup: a tuple

	returns: tuple, every other element of aTup. 
	'''
	# Your Code Here
	ret = []
	count = 0
	for x in aTup:
		if count % 2:
			print(x)
			ret.append(x)
			print('Here: ' +  str(x))
		count += 1
	return ret

temp = oddTuples((8, 13, 7, 0, 20, 20, 4, 8))
print(temp)