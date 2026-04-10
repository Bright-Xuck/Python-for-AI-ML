i = 1
while i < 6:
  print(i)
  i+1

j = 1
while j < 6:
  print(j)
  if j == 3:  #This is to break when j reaches 3 so the output will be 1,2,3
    break  ## the break statement will stop the loop even if the conditions are true
  j += 1  


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue  ##With the continue statement we can stop the current iteration, and continue with the next: 
  print(i)    ##so there wont be a 3 in the results