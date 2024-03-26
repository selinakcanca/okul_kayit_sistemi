class Teacher:

 def __init__(self, name, age, department) -> None:
    self.name = name
    self.age = age
    self.department = department
    print("Yapıcı blok çalıştı")

 def doAttend(self, message):   #yoklama aldı mı?
    print(f"{self.name} {self.age} {self.department} : {message}" )

 def examCheck(self):  #sınavı kontrol etti mi?
    print(f"{self.name} is checking exams")


