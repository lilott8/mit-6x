def isIn(char, aStr):
	'''
	char: a single character
	aStr: an alphabetized string

	returns: True if char is in aStr; False otherwise
	
	We need to test for in string and not in string
	'''
	# Your code here
	#accomodate a strlen of 0
	if len(aStr) == 0:
		return False
	#accomodate a strlen of 1
	elif (len(aStr) == 1) and char == aStr:
		return True
	elif (len(aStr) == 1) and char != aStr:
		return False
	else:
		#bisect the string here
		high = int(len(aStr))
		middle = int(round((high / 2), 0))
		#print("High: ", str(high))
		#print("Middle: ", str(middle))
		#print("String: ", aStr)
		#print("**********************")
		if char > aStr[middle]:
			return isIn(char, aStr[middle:high])
		elif char < aStr[middle]:
			return isIn(char, aStr[0:middle])
		else:
			return True
			
print(str(isIn('f', 'ceffgijqsvxy')))