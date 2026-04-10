fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#We can use the continue to skip a particular block of code when a particular condition is met

fruit = ["apple", "banana", "cherry"]
for y in fruit:
  if y == "banana":
    continue
  print(x)

#The range method can also be used 
for x in range(6):  # also something like range(2,6)
  print(x)
else:
  print("Finally finished!")  