def isWordGuessed(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: boolean, True if all the letters of secretWord are in lettersGuessed;
	False otherwise
	'''
	# FILL IN YOUR CODE HERE...
	count = 0
	length = len(secretWord)
	for x in lettersGuessed:
		if x in secretWord:
			count += 1
	if length == count:
		return True
	else:
		return False


#print isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
#print isWordGuessed('carrot', ['s', 'e', 'w', 'o', 'v', 'd', 'r', 'h', 'y', 'l'])
#print isWordGuessed('lettuce', ['z', 'x', 'q', 'l', 'e', 't', 't', 'u', 'c', 'e'])