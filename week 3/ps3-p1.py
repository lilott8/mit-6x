def evaluatePoly(poly, x):
	'''
	Computes the value of a polynomial function at given value x. Returns that
	value as a float.
 
	poly: list of numbers, length > 0
	x: number
	returns: float
	'''
	answer = 0.00
	count = 0
	for y in poly:
		answer += y * (x**count)
		count += 1.0
	return answer
	
	
print evaluatePoly([0.0, 0.0, 5.0, 9.3, 7.0], -13)
print evaluatePoly([2, 0, 7, 1], 4)
print evaluatePoly([-12], 3.7)