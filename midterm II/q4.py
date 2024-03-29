class Person(object):
    def __init__(self, name):
        self.name = name
    def __lt__(self, other):
        return self.name < other.name
    def __str__(self):
        return self.name
    def getName(self):
        return self.name

class edXPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = edXPerson.nextIdNum
        edXPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        if self.idNum == other.idNum:
            return self.getName() < other.getName()
        else:
            return self.idNum < other.idNum
    def isStudent(self):
        return isinstance(self, Student)
class Student(edXPerson):
    pass

class UniversityStudent(Student):
    pass

class SelfLearner(Student):
    def __init__(self, name):
        Student.__init__(self, name)
        self.idNum = 0

class Subject(object):
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)

    def allStudents(self):
        self.students.sort(key=lambda self: (self.idNum, self.name))
        for x in range(len(self.students)):
            yield self.students[x]
    def __str__(self):
        return 'Subject with ' + str(len(self.students)) + ' students.'
        

p1 = edXPerson('Fred Flintstone')
p2 = UniversityStudent('Wilma Flintstone')
p3 = Student('Betty Rubble')
p4 = SelfLearner('Barney Rubble')
p5 = SelfLearner('Dino')
p = Person('Eric Grimson')

'''
mySubject = Subject()
mySubject.addStudent(p1)
mySubject.addStudent(p2)
mySubject.addStudent(p3)
mySubject.addStudent(p4)
mySubject.addStudent(p5)
#mySubject.addStudent(p)
print "Should print:"
print "Barney Rubble - " + str(p4.idNum)
print "Dino - " + str(p5.idNum)
print "Fred Flintstone - " + str(p1.idNum)
print "Wilma Flintstone - " + str(p2.idNum)
print "Betty Rubble - " + str(p3.idNum)
print "+++++++++++++++++++++++++++"
for s in mySubject.allStudents():
    print s
'''