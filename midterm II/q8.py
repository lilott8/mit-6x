def probTest(limit):
    if limit > 1:
        limit = 1
    #number of rolls
    n = 1.0
    #this is a constant based on the fact that we don't want
    #to see a "1" until the nth value
    probability = 5.0/6.0
    while (probability**(n-1)*(1-probability)) >= abs(limit):
        #increase the number of rolls
        n+=1.0
    return n-1
    
print probTest(.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)