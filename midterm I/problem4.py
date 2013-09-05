def laceStrings(s1, s2):
    laced = ''
    string1 = list(s1)
    string2 = list(s2)
    
    for i in range(0,len(s1)):
        if len(string1) > 0:
            laced += string1[0]
            del string1[0]
        if len(string2) > 0:
            laced += string2[0]
            del string2[0]
    if len(string2) > 0:
        laced += "".join(string2)
    return laced
    
print laceStrings("jason", "shelley")
print laceStrings('jasper', 'pie')
print laceStrings('as', 'a')
print laceStrings('asdfsdafsdfas', 'r')
print laceStrings('a','asdfasdfasdfasdf')