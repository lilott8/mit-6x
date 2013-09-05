num = float(raw_input("What is the number: "))
middle = num/2
iterations = 0
min = 0
max = num

while middle**2 != num:
	print("Min: " + str(min))
	print("Middle: " + str(middle))
	print("Max: " + str(max))
	print("Number of iterations: " + str(iterations))
	print("=================")
	iterations += 1
	if middle**2 > num:
		max = middle
	else:
		min = middle
	middle = (max + min) / 2
	
print("Square Root of " + str(num) + " is: " + str(middle))
print("It took: " + str(iterations) + " iterations")
