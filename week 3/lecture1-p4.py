def gcdRecur(a, b):
	'''
	a, b: positive integers
	
	returns: a positive integer, the greatest common divisor of a & b.
	'''
	# Your code here
	if b == 0:
		return a
	else:
		temp = b
		b = a % b
		a = temp
		return gcdRecur(a, b)

	
	
print(str(gcdRecur(2, 12)))
print(str(gcdRecur(6, 12)))
print(str(gcdRecur(9, 12)))
print(str(gcdRecur(17, 12)))