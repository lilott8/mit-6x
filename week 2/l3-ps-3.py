'''
320000, .2, 29157.09
*******
999999, .18, 90325.07
'''
balance = 320000
annualInterestRate = .2
mir = annualInterestRate / 12
high = (balance * ((1 + mir)**12)) / 12
low = balance / 12.0
middle = (high + low) / 2.0
epsilon = .01
originalBalance = balance

while balance > 0:
	#make sure our middle pays or debt
	for month in range(12):
		balance =  (balance - middle) * (1+mir)
	#if it doesn't, lets change our binary search
	if abs(balance) > epsilon:
		#change our low if we still have a balance
		if balance > 0:
			low = middle
		#if we don't have a balance then our high is too high
		else:
			high = middle
		#recalculate middle
		middle = (high + low) / 2.0
		#set balance back to the test case
		balance = originalBalance
	else:
		print("Lowest Payment: " + str(round(middle,2)))
		break