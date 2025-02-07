class Student:

    class_year = 2024
    num_student = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_student+=1

student1 = Student("Spongebob",30)
studen2 = Student("Patrick",25)
student3 = Student("squidward",20)
print(f"My graduating class of {Student.class_year} has {Student.num_student} students")

print(student1.name)
print(studen2.name)
print(student3.name)