def getAvailableLetters(lettersGuessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
	yet been guessed.
	'''
	# FILL IN YOUR CODE HERE...
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for letter in lettersGuessed:
		alphabet = alphabet.replace(letter, '')
	return alphabet
	
print getAvailableLetters(['a', 'h', 'l', 'x', 'f'])