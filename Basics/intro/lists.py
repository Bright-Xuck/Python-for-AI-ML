#Lists are arrays
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.append("youurt--")
print(thislist)

#Go through the various methods for lists

#To check if the item exist in the list
if "apple" in thislist:
    print("Apple is in the list")

#loop through lists
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])  

#append method to add an iten to the end of a list
thislist.append("Peach")
print(thislist)    

#extend method to add items from another list to the present list
thatlist = ["one", "two"]
thislist.extend(thatlist)
print(thislist)

#sort method sorts the list alpha and to do in reverse .sort(reverse = true)