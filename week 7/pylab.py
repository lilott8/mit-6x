import matplotlib as mpl
import matplotlib.pylab as pylab

principal = 10000
interestRate = .05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(range(years + 1), values, 'ro')
pylab.title("Compound Interest")
pylab.xlabel("Years")
pylab.ylabel("Amount")
pylab.show()
