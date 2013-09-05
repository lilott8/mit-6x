def computeDeriv(poly):
	'''
	Computes and returns the derivative of a polynomial function as a list of
	floats. If the derivative is 0, returns [0.0].
 
	poly: list of numbers, length &gt; 0
	returns: list of numbers (floats)
	'''
	# FILL IN YOUR CODE HERE...
	deriv = []
	count = 0.0
	temp = 0
	length = len(poly)
	for x in poly:
		#normal: a*b^x
		#deriv: (x*a)b^(x-1)
		#if length is 1, then we append the 0.0
		if length == 1:
			deriv.append(0.0)
		#This case ignores the first polynomial that gets chopped of
		#given a polynomial derivative
		elif count == 0.0:
			temp = 1
		else:
			deriv.append(count * x)
		count += 1
	return deriv
	
print computeDeriv([-13.39, 0.0, 17.5, 3.0, 1.0])
print computeDeriv([6, 1, 3, 0])
print computeDeriv([20])