def McNugget(n):
    sizes = [0,0,0]
    while n > 5:
        if n % 20 == 0:
            sizes[2] += 1
            n -= 20
        elif n % 9 == 0:
            sizes[1] += 1
            n-=9
        else:
            sizes[0] += 1
            n-=6
    nuggets = (6*sizes[0]) + (9*sizes[1]) + (20*sizes[2])
    if nuggets == n:
        return True
    else:
        return False
    
print "Trial 1: "+ str(McNugget(43))#t
print "Trial 2: "+str(McNugget(18))#t
print "Trial 3: "+str(McNugget(12))#t
print "Trial 3: "+str(McNugget(24))#t
print "Trial 4: "+str(McNugget(49))#t
print "Trial 5: "+str(McNugget(9))#t
'''
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