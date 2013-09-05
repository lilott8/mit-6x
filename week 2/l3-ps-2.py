balance = 3926
annualInterestRate = .2
minMonth = 10
monthlyInterestRate = annualInterestRate / 12

while True:
    bal = balance
    for month in range(1, 13, 1):
        bal = (bal - minMonth) * (1 + monthlyInterestRate)
    if bal < 0:
        break
    minMonth += 10
print('Lowest Payment: ' + str(minMonth))