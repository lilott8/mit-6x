import pylab, random
def doit():
    a = 1.0
    b = 2.0
    c = 4.0
    yVals = []
    xVals = range(-20, 20)
    for x in xVals:
        yVals.append(a*x**2 + b*x + c)
    yVals = 2*pylab.array(yVals)
    xVals = pylab.array(xVals)
    try:
        a, b, c, d = pylab.polyfit(xVals, yVals, 3)
        print a, b, c, d
    except:
        print 'fell to here'
        
for x in range(10):
    print doit()