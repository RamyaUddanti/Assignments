class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = " "

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

obj = Student()
obj.setName(input("Enter student name: "))
obj.setRollNumber(input("Enter student roll number: "))

print("Student Name:", obj.getName())
print("Student Roll Number:",obj.getRollNumber())