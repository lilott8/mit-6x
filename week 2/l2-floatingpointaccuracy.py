def whole_number(num):
	result = '0'
	num = int(num)
	if num < 0:
		isNeg = True
		num = abs(num)
	else:
		isNeg = False
	if num == 0:
		result = '0'
	while num > 2:
		result = str(num%2) + result
		num = num/2
	if isNeg:
		result = '-' + result
	print("Given a whole number, " + str(num) + " this is the binary representation: " + str(result))
	
def fraction(num):
	p = 0
	result = '0'

	while((2**p)*num)%1 != 0:
		print("Remainder= " + str((2**p)*num - int((2**p)*num)))
		p += 1

	num = int(num*(2**p))
	
	if num == 0:
		result = '0'
	while num > 0:
		result = str(num%2) + result
		num = num/2
	for i in range(p - len(result)):
		result = '0' + result
	result = result[0:-p] + '.' + result[-p:]
	print("Given a decimal number, " + str(num) + " this is the binary represenataion: " + str(result))

num = float(raw_input("What number: "))

if num < 1 and num > 0:
	fraction(num)
else:
	whole_number(num)
