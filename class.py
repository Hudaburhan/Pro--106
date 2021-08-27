class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name= name
        self.age= age
        self.gender= gender
        self.level= level
        self.grades = grades or {}
        
    def setGrade(self, course, grade):
        self.grades[course]= grade
        
    def getGrade(self, course):
        return self.grades[course]
    
    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)


# Defining object of Student class
john= Student("John", 12, "Male", 6 , {"math":3.3})
jane= Student("jane", 12, "Female", 6 , {"math":3.5})
john.setGrade("science", 5)
print(john.getGrade("science"))
    