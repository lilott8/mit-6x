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
	
def hangman(secretWord):
	'''
	secretWord: string, the secret word to guess.

	Starts up an interactive game of Hangman.

	* At the start of the game, let the user know how many 
		letters the secretWord contains.

	* Ask the user to supply one guess (i.e. letter) per round.

	* The user should receive feedback immediately after each guess 
		about whether their guess appears in the computer’s word.

	* After each round, you should also display to the user the 
		partially guessed word so far, as well as letters that the 
		user has not yet guessed.

	Follows the other limitations detailed in the problem write-up.
	'''
	# FILL IN YOUR CODE HERE...
	length = len(secretWord)
	lettersGuessed = []
	turns = 8
	mistakesMade = 0
	print("I am thinking of a word that is " + str(length) + " letters long.")
	print '-------------'
	while not isWordGuessed(secretWord, lettersGuessed) and turns != 0:
		print "You have " + str(turns) + " left."
		print("Available letters: " + getAvailableLetters(lettersGuessed))
		guess = raw_input("Please guess a letter: ")
		guess = guess.lower()
		#See if our guess has been guessed
		if guess in lettersGuessed:
			lettersGuessed.append(guess)
			print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
			mistakesMade += 1
			turns -= 1
		else:
			lettersGuessed.append(guess)
			if guess in secretWord:
				print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
			else:
				print "Oops! That letter is not in my word " + getGuessedWord(secretWord, lettersGuessed)
				turns -= 1
		print '-------------'
	if isWordGuessed(secretWord, lettersGuessed) and turns > 0:
		print "Congratulations, you won!"
	else:
		print "Sorry, you ran out of guesses. The word was " + secretWord
	return 1
hangman('seven')