from student import Student 


student1=Student("Büşra", 25)   
student1.doHomework("Ödevi yaptım")
student1.study()


student2=Student("Sümeyye", 25)   
student2.doHomework("Ödevi yaptım")
student2.study()



from teacher import Teacher

teacher1=Teacher("Neşe", 25, "Math")   
teacher1.doAttend("Yoklama aldı")
teacher1.examCheck()


teacher2=Teacher("Selin", 29, "Art")   
teacher2.doAttend("Yoklama almadı")
teacher2.examCheck()


Student = ["Büşra","Sümeyye"]
Student.append("Züleyha")
print(Student)


list = []
list.append (student1)
list[0].age




