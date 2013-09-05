from ps4a import *
import time
from perm import *


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all possible 
    permutations of lengths 1 to HAND_SIZE.

    If all possible permutations are not in wordList, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create an empty list to store all possible permutations of length 1 to HAND_SIZE
    list = [range(1,HAND_SIZE+1)]
    current_score = 0
    max_score = 0
    best_word = None
    # For all lengths from 1 to HAND_SIZE (including! HAND_SIZE):
    for word in wordList:
        # Get the permutations of this length
        if len(word) <= HAND_SIZE:
            if isValidWord(word, hand, wordList) is True:
                current_score = getWordScore(word, HAND_SIZE)
                if current_score > max_score:
                    max_score = current_score
                    best_word = word
        # And store the permutations in the list we initialized earlier
        #  (hint: don't overwrite the list - you want to add to it)


    # Create a new variable to store the maximum score seen so far (initially 0)
    #max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    #best_word = None

    # For each possible word permutation:
    #for word in list:
        # If the permutation is in the word list:
            
            # Get the word's score

            # If the word's score is larger than the maximum score seen so far:

                # Save the current score and the current word as the best found so far



    # return the best word seen
    return best_word
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    # TO DO ... <-- Remove this comment when you code this function
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    print "playGame not yet implemented." # <-- Remove this when you code this function

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    #playGame(wordList)
    compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList)
    compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList)
    compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList)
    compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList)

    print "Goodbye!"
