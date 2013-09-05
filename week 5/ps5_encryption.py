# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random
import re

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    shifted = {}
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    for i in lowercase:
        #Convert the character to an int
        char = ord(i)
        #see if we are greater than 122 (ascii z)
        if char + shift >= 123:
            char = abs(((char + shift) - 122 ) + 96)
            shifted[i] = str(unichr(char))
        #if not then we just perform a normal shift
        else:
            shifted[i] = str(unichr(char + shift))
    for i in uppercase:
        #Convert the character to an int
        char = ord(i)
        #see if we are greater than 90 (ascii Z)
        if char + shift >= 91:
            char = abs(((char + shift) - 90 ) + 64)
            shifted[i] = str(unichr(char))
        #if not then we just perform a normal shift
        else:
            shifted[i] = str(unichr(char + shift))
    return shifted

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    string = ''
    for i in text:
        ascii = ord(i)
        if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122): 
            string += coder[i]
        else:
            string += i
    return string

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    split = text.split(' ')
    words = []
    length = 0
    word_to_decrypt = ''
    #just grab the longest word to decrypt (this will ensure we are correct)
    for i in split:
        if len(re.sub(r'\W+', '', i)) > 3:
            words.append(i)
    #check the decryption
    for word in words:
        for i in range(26):
            decrypted = applyCoder(re.sub(r'\W+', '', word), buildCoder(i))
            if isWord(wordList, decrypted):
                return i
    return "nothing found"

def decryptStory(wordList):
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    story = getStoryString()
    ceasar = findBestShift(wordList, story)
    return applyShift(story, ceasar)
    #return "Not yet implemented." # Remove this comment when you code the function

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    print decryptStory(wordList)
    #ceasar = findBestShift(wordList, 'Tkmu Pvyboi')
    #print applyShift('Tkmu Pvyboi', ceasar)
