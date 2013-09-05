def isPrime(n):
    if type(n) != int:
        raise TypeError
    if n <=0:
        raise ValueError
    if n==1:
        return False
    else:
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                return False
        return True
            
            
#isPrime(5.54)
print isPrime(13)
print isPrime(27)
print isPrime(125)
#isPrime([1,2,3])