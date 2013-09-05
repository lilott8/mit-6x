x= int(raw_input("Enter an interger: "))
ans = 0
for ans in range(0, abs(x)+1):
	ans += 1
if ans**3 != abs(x):
	print(str(x) + ' is not a perfect cube')
else:
	if x < 0:
		ans = -ans
	print('Cube root of ' + str(x) + ' is ' + str(ans))
