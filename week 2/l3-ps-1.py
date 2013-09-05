balance = 5000.00
apr = .18
monthly_rate = .02
minimum_due = .02 
month = 0
interest_paid = 0
payment = 0
annualInterestRate = .18
running_payment = 0

while month < 12:
    payment = balance * .02;
    running_payment += payment
    balance = (balance - payment) * (1+(annualInterestRate/12))
    month += 1
print("Total paid: " + str(round(running_payment,2)))
print("Remaining balance: " + str(round(balance,2)))


"""
while month <= 12:
	payment = (minimum_due * balance)
	running_payment += payment
	interest_paid = (balance - payment) * (apr/12)
	balance = ( balance - payment ) * ( 1 + (apr/12))
	month += 1
	print("Balance remaining: " + str(round(balance,2)))
	print("Payment made: " + str(round(payment, 2)))
	print("Interest paid: " + str(round(interest_paid, 2)))
	print("=================")
print("Total payment: " + str(round(running_payment,2)))
"""
