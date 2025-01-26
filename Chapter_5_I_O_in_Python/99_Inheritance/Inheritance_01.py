class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping....")

class Student(People):
    def __init__(self, name, age, student_id):
        People.__init__(self, name, age)
        self.student_id = student_id

student_one = Student("Wilson", 25, 100)
print(student_one.name)
print(student_one.age, student_one.student_id)
student_one.sleep()