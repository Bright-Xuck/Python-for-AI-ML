#create a class that interates through numbers 1 to 5 and prints them
class Iteration:
    def __init__(self, next):
        self.next = next 

    def inter(self):
        self.next = self.next + 1
        print(self.next)

x = Iteration(0)
while (x.next < 5):
 x.inter()            


# class Bright:
#    def __init__(self, name, age):
#      self.name = name
#      self.age = age

# new = Bright("Lemuel", 3)
# print(new)

