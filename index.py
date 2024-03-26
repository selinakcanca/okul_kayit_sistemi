from student import Student 
from teacher import Teacher

studentList = []
teacherList = []

student1 = Student("Büşra, 25")
student2 = Student ("Sümeyye, 25")


teacher1 = Teacher ("Neşe","math")
teacher2 = Teacher ("Selin","art")


def add(type,obj):
    if type == "student":
       studentList.append(obj)
    else:
        teacherList.append(obj)   



def getAll(type):  
    if type == "teacher":
        for teacher in teacherList:
            print(teacher.name)
    else:
        for student in studentList:
            print(student.name)


add("student",student1)
add("teacher",teacher1)    
add("student",student2)
add("teacher",teacher2)                   

getAll("student")
getAll("teacher")

print(studentList)
print(teacherList)