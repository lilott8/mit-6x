def recurPower(base, exp):
	'''
	base: int or float.
	exp: int >= 0
	returns: int or float, base^exp
	'''
	#accomodate for n^0
	if exp == 0:
		return 1
	#accomodate for n^1
	elif exp >= 2:
		return base * recurPower(base, exp - 1)
	#all other cases: n^y where y > 1
	else:
		return base
		
		
temp1 = recurPower(-9.46, 0)
temp2 = recurPower(-8.23, 1)
temp3 = recurPower(9.06, 2)
temp4 = recurPower(-4.29, 8)

print(str(temp1))
print(str(temp2))
print(str(temp3))
print(str(temp4))