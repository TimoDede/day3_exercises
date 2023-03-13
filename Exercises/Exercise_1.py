class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def full_name(self):
        return "%s %s" % (self.firstname, self.lastname)

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject

    def printNameSubject(self):
        return "%s %s, %s" %(self.firstname, self.lastname, self.subject)

class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course

    def printNameCourse(self):
        return "%s %s, %s" %(self.firstname, self.lastname, self.course)

name = Person("Timo", "Dederichs")
print(name.full_name())

name = Student("Timo", "Dederichs", "Physics")
print(name.printNameSubject())

name = Teacher("Filipe", "Maia", "Python Course")
print(name.printNameCourse())