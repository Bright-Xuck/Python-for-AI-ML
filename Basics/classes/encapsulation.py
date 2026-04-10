#encapsulation is basically restricting the access other classes nad varaibles have to a particular class' attributes and methods

class Encapsulation:
    def __init__(self, name, age):
        self._name = name
        self._age = age

Person = Encapsulation("Lemuel", 70)
print(Person.name)
       
