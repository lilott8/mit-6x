"""
Simple Case: cx^2 + k
First derivative: 2cx
if polynomail is x^2+k then derivative is 2x
Formula for finding the root:
g - g(^2-k)/2g where "k" is the number you want the square root of
in this program, y = k
"""
epsilon = .01
y=25.0
guess = y/2.0
iteration = 0

while abs(guess*guess - y) >= epsilon:
	guess = guess - (((guess**2) - y)/(2*guess))
	iteration += 1
print("Squre root of " + str(y) + ' is about ' + str(guess))
print("It took: " + str(iteration) + " iterations to find the solution")
