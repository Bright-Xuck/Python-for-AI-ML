# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

#classes in python are just like objects in js
# tomake private classes and attributes in python we use an underscore before the varaible name to make them private eg self._name or class _Bright

class Person:
  def __init__(self, name, age):
    self.name = name  #self.name = name:
    self.age = age    #self.age = age:

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Name:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def printname(self):
    print(self.fname, self.lname)    

x = Name("Njikang", "Bright")
x.printname()

##Inheritance   #creating a chuld class that inherits the properties of the parent class
##We pass the parent class as a property to the child class

class student(Name):
  def __init__(self, fname, lname): #we can replace these entire two lines with pass if we dont want to add anything new and just use the parents objects
    Name.__init__(self, fname, lname)  #the def in line33 overwrites the parenst so we need to add another def in line34
    self.year = 2018

  def welcome(self):
    print("Welcomes to brights code")

x = student("Mike", "Olsenjbjbhjhbjhn")
x.printname()
print(x.year)
x.welcome()


