from __future__ import generators

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

def getPerms(hand, n):
    """
    Takes in the current hand and a number.  It returns all
    possible permutations of size n given the letters in the hand.

    If n > len(hand), returns an empty list.
 
    hand: dictionary (string -> int)
    n: int 
    returns list (string)
    """

    if n > sum([val for val in hand.values()]):
        return []

    handlist = []
    
    for key in hand:
	for i in range(hand[key]):
	    handlist.append(key)
    l = [] 
    toret = []
    for c in xuniqueCombinations(handlist,n):
	l.append(c)
    for j in l:
        for p in xpermutations(j):
            toret.append("".join(p))
    return toret	

if __name__=="__main__":
    print "Permutations of 'love'"
    for p in xpermutations(['l','o','v','e']): print ''.join(p)

    print
    print "Combinations of 2 letters from 'love'"
    for c in xcombinations(['l','o','v','e'],2): print ''.join(c)

    print
    print "Unique Combinations of 2 letters from 'love'"
    for uc in xuniqueCombinations(['l','o','v','e'],2): print ''.join(uc)

    print
    print "Selections of 2 letters from 'love'"
    for s in xselections(['l','o','v','e'],2): print ''.join(s)

    print
    print map(''.join, list(xpermutations('done')))

    print "testing stuff for 6.00"
    print len(getPerms({"a":2, "b":3, "c":1}, 3))

    print "testing stuff for 6.00"
    print len(getPerms({"a":2, "b":3, "c":1}, 6))

    print "testing stuff for 6.00"
    print len(getPerms({"a":2, "b":3, "c":1}, 7))
