def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    temp = b
    i=1
    #if x < b:
    #    return 1
    while b*temp <= x:
        b *= temp
        i+=1
    return i
    
print myLog(16,2) #should be 4
print myLog(15,3) #should be 2
print myLog(72,4) #should be
print myLog(1,2)
print myLog(44938,99)
print myLog(255,2)