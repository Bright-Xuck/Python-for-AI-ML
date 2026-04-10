import numpy as np

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = [int(g) for g in grade]

    def  printdetails(self):
        print("name:", self.name,",", "grades:", self.grade)


def populate():
 grades = []
 Person = None   

 print("Enter your name")
 name = input()

 print("Enter the grades in 5 courses")
 for i in range(3):
    b = input()
    grades.append(b)

 Person = Student(name, grades)
 return Person

Person1 = populate()
Person2 = populate()
Person3 = populate()

finalgrades = np.concatenate((Person1.grade, Person2.grade, Person3.grade))
finalgrades = finalgrades.reshape(3,3)

print("Student Analysis")
print(Person1.name, np.sum(Person1.grade), np.mean(Person1.grade))
print(Person2.name, np.sum(Person2.grade), np.mean(Person2.grade))
print(Person3.name, np.sum(Person3.grade), np.mean(Person3.grade))

print('Course analysis')
for j in range(3):
   for k in range(3):
    print(f`course at index ${j}`, finalgrades[k, j])