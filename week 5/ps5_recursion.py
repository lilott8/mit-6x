# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr, newString=''):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    reverse = list(aStr)
    if len(reverse) > 0:
        newString += reverse[-1]
        return reverseString(''.join(reverse[:len(reverse)-1]), newString)
    else:
        return newString
#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO.
    xian = list(x)
    word_list = list(word)
    if len(xian) < 1:
        return True
    elif len(word_list) < 1:
        return False
    elif xian[0] != word_list[0]:
        return x_ian(xian[0:], word_list[1:])
    elif xian[0] == word_list[0]:
        return x_ian(xian[1:], word_list[1:])
    else:
        return False
    
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
    if len(text) < lineLength:
        return text
    else:
        #Take the characters necessary for our linelength and keeping the whole word
        newtext = text[text[lineLength-1:].find(' ') + lineLength:]
        endLine = text[lineLength-1:].find(' ')
        if endLine < 0:
            print endLine
            endLine = text[lineLength-1:]
            print endLine
        else:
            endLine = text[lineLength-1:].find(' ') + lineLength
        #endline += lineLength
        if endLine < lineLength:
            print endLine
            endLine = lineLength
        return text[:endLine] + '\n' + insertNewlines(newtext, lineLength)

    

#print reverseString('jason')
#print x_ian('eric', 'algebraic')
#print x_ian('alvin', 'palavering')
#print x_ian('sarina', 'czarina')
#print x_ian('john', 'mahjong')
print insertNewlines('Random text to wrap again.', 5)