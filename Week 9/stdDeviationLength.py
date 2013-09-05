def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    total = 0.0
    length = len(L)
    if length < 1:
        return float('NaN')
    else:
        lengthList = []
        for y in L:
            lengthList.append(len(y))
        mean = sum(lengthList)/float(length)
        for x in lengthList:
            total += (x-mean)**2
        return (total/length)**0.5