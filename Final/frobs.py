class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    1)check where the newFrob belongs
        1)iterate all frobs until newFrob > frob.getBefore
        2)insert the frob
        3)change the frob before and frob after
    
    """

    #Checks for nothing in our list
    if atMe.getBefore() is None or atMe.getAfter() is None:
        if atMe.myName() > newFrob.myName():
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
        else:
            newFrob.setBefore(atMe)
            atMe.setAfter(newFrob)
    else:
        if atMe.myName() < newFrob.myName():
            iterateToEnd(atMe, newFrob)
        else:
            iterateToBegin(atMe, newFrob)
        
def iterateToBegin(atMe, newFrob):
    newBefore = atMe.getBefore()
    while newFrob.getName() <= newBefore.getName() or newBefore is not None:
        if newBefore.getBefore() is not None:
            newBefore = newBefore.getBefore()
        else:
            break
    newAfter = newBefore.getAfter()
    newBefore.setAfter(newFrob)
    newAfter.setBefore(newForb)
    
def iterateToEnd(atMe, newFrob):
    newAfter = atMe.getAfter()
    if newAfter is not None:
        while newFrob.myName() >= newAfter.myName() or newAfter is not None:
            if newAfter.getAfter() is not None:
                newAfter = newAfter.getAfter()
                print newAfter.myName()
            else:
                break
    else:
        newAfter = atMe
    newBefore = newAfter.getBefore()
    newBefore.setAfter(newFrob)
    newAfter.setBefore(newFrob)

    
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, martha)
insert(eric, ruth)
print eric.getAfter().myName()
#insert(eric, ruth)
print ruth.getAfter().myName()
insert(eric, fred)
#insert(eric, eric)





"""
 newBefore = atMe.getBefore()
    newAfter = atMe.getAfter()
    print newBefore
    if newBefore is None and newAfter is None:
        if atMe < newFrob:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
    if atMe < newFrob and newAfter is not False:
        #iterate the double linked list towards beginning
        while newFrob < newBefore.getBefore() or newBefore.getBefore() is not None:
            newBefore = newBefore.getBefore()
        newAfter = newBefore.getAfter()
        newBefore.setAfter(newFrob)
        newAfter.setBefore(newForb)
    else:
        #iterate the double linked list towards end
        while newFrob > newAfter.getAfter() or newAfter.getAfter() is not None:
            newAfter = newAfter.getAfter()
        newBefore = newAfter.getBefore()
        newBefore.setAfter(newFrob)
        newAfter.setBefore(newFrob)
"""