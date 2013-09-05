def getGuessedWord(secretWord, lettersGuessed):
	'''
	return true if lettersGuessed is secretWord
	else false
	'''
	z = 0
	checker = []
	while z < len(secretWord):
		checker.append('')
		z += 1
	for x in lettersGuessed:
		count = 0
		for y in secretWord:
			if x == y:
				checker[count] = y
			count += 1
	z=0
	while z < len(checker):
		if checker[z] == '':
			checker[z] = '_'
		z += 1
	return ''.join(checker)