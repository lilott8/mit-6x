def iterPower(base, exp):
	'''
	base: int or float.
	exp: int >= 0
	returns: int or float, base^exp
	'''
	i = exp
	orig = base
	#accomodate for n^0
	if exp == 0:
		return 1
	#accomodate for n^1
	elif exp == 1:
		return orig
	#all other cases: n^y where y > 1
	else:
		while i > 1:
			base = base * orig
			i -= 1
		return base
		
		
temp1 = iterPower(-9.46, 0)
temp2 = iterPower(-8.23, 1)
temp3 = iterPower(9.06, 2)
temp4 = iterPower(-4.29, 8)

print(str(temp1))
print(str(temp2))
print(str(temp3))
print(str(temp4))