#def to create a function
def myfunction():
    print("Hello world")

myfunction()

def yourfunction(name):
    print("Hello world" + " " + name)

yourfunction("Mary")

#we use * before an argument when we dont know how many paramneters will be passed eg *kids
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# We can also pass in list and other composite data types into functions as arguments an dperform computataions on the them
def m_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

m_function(fruits)

#funtions can alos return values
def y_function(x):
  return 5 * x

print(y_function(3))
print(y_function(5))
print(y_function(9))
