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

def computeRoot(poly, x_0, epsilon):
	'''
	Uses Newton's method to find and return a root of a polynomial function.
	Returns a list containing the root and the number of iterations required
	to get to the root.

	poly: list of numbers, length > 1.
	Represents a polynomial function containing at least one real root.
		The derivative of this polynomial function at x_0 is not 0.
	x_0: float
	epsilon: float > 0
	returns: list [float, int]
	'''
	# FILL IN YOUR CODE HERE...
	trials = 0
	def rootCheck(poly, x_0, epsilon, trials):
		fx = evaluatePoly(poly, x_0)
		print ("fx: " + str(fx))
		print ("Epsilon: " + str(epsilon))
		#Check for us meeting our goal on unperfect squares
		if abs(fx) < epsilon and abs(fx) > 0.0:
			return [x_0, trials]
		#check for perfect squares
		elif fx == 0:
			return [x_0, trials]
		#otherwise try again.
		else:
			print str(trials)
			fx_deriv = evaluatePoly(computeDeriv(poly), x_0)
			print("fx_deriv: " + str(fx_deriv))
			x_0 = x_0 - (fx / fx_deriv)
			print ("x_0: " + str(x_0))
			return rootCheck(poly, x_0, epsilon, trials+1)
	return rootCheck(poly, x_0, epsilon, trials)

	
	
	
print computeRoot([-8,2,1],-4,.0001)
#print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)
#print computeRoot([1, 9, 8], -3, .01)
#print computeRoot([1, -1, 1, -1], 2, .001)