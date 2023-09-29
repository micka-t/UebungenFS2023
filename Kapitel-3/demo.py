class Student:
    def __init__(self, name,vorname):
        self.name = name
        self.vorname = vorname

class Dozent:
    def __init__(self, name,vorname):
        self.name = name
        self.vorname = vorname

class Programmierkurs:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def addStudent(self, stud):
        self.students.append(stud)

kurs = Programmierkurs("GeoProgrammierung 1")

stud1 = Student("Müller", "Anna")
stud2 = Student("Meier", "Hans")

kurs.addStudent(stud1)       
kurs.addStudent(stud2)     