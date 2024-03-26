
class Student:

 def __init__(self, name, age) -> None:
    self.name = name
    self.age = age
    print("Yapıcı blok çalıştı")

 def doHomework(self, message):
    print(f"{self.name} : {message}")

 def study(self):
    print(f"{self.name} is Studying...")




