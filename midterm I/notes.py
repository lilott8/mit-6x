import math
def McNugget(n):
    if n < 6:
        return False
    while n > 0:
        print n
        if n % 20 == 0:
            n -= 20
        elif n % 9 == 0:
            n -= 9
        elif n % 6 == 0:
            n -= 6
        elif n >= 20:
            n -= 20
        elif n >= 9:
            n -= 9
        elif n >= 6:
            n -= 6
        else:
            return False
    if n == 0:
        return True
    else:
        return False

        
def laceStringsRecur(s1, s2):
    '''
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    '''
    def helpLaceStrings(s1, s2, out):
        #print s1
        #print s2
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:],s2[1:],out + s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')

    
    
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    temp = b
    i=1
    if x < b:
        return 0
    while b*temp <= x:
        i+=1
        b *= temp
    return i
print myLog(16,2) #should be 4
print myLog(15,3) #should be 2
print myLog(16,4)
print myLog(15,16)

'''    
print myLog(2,2) #should be
#print myLog(0,2)
print myLog(44938,99)
print myLog(255,2)
'''

'''
print "Trial 1: "+ str(McNugget(43))#t
print "Trial 2: "+str(McNugget(18))#t
print "Trial 3: "+str(McNugget(12))#t
print "Trial 3: "+str(McNugget(24))#t
print "Trial 4: "+str(McNugget(49))#t
print "Trial 5: "+str(McNugget(9))#t
print "Trial 6: "+str(McNugget(21))#f
print "Trial 7: "+str(McNugget(36))#t
print "Trial 8: "+str(McNugget(14))#f
print "Trial 9: "+str(McNugget(2000))#t
print "Trial 10: "+str(McNugget(-6))#f
print "Trial 11: "+str(McNugget(20))#t
print "Trial 12: "+str(McNugget(12345152))#t
print "Trial 13: "+str(McNugget(9.0))#t
print "Trial 14: "+str(McNugget(9.1))#t
print "Trial 15: "+str(McNugget(0))#t
'''
'''
print laceStringsRecur('jason', 'shelley')
print laceStringsRecur('abcd', 'efgh')
print laceStringsRecur('abc', 'defghijk')
print laceStringsRecur('abcdefgh', 'ijk')
'''