def recurPowerNew(base, exp):
	'''
	base: int or float.
	exp: int >= 0
	returns: int or float, base^exp
	'''
	#accomodate for n^0
	if exp == 0:
		return 1
	#all other cases: n^y where y > 1
	elif exp % 2 == 1:
		#base * base^(exp-1)
		return base * recurPowerNew(base, exp - 1)
	else:
		#base^exp = (base^2)^(exp/2)
		return recurPowerNew(base * base, exp / 2)

temp1 = recurPowerNew(7.18, 0)
temp2 = recurPowerNew(-7.64, 1)
temp3 = recurPowerNew(4.76, 5)
temp4 = recurPowerNew(-2.8, 1)
temp5 = recurPowerNew(6.34, 7)

print(str(temp1))	#Should be: 1.0000
print(str(temp2))	#Should be: -7.6400
print(str(temp3))	#Should be: 2443.6261
print(str(temp4))	#Should be: -2.8000
print(str(temp5))	#Should be: 411741.6544