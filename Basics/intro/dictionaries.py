#dictionaries are basically ojects
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#To acces item here we have too reference its name in square brackets
x = thisdict["brand"]
print(x)

thisdict["model"]= "Newshit"

#keys method
y = thisdict.keys()
print(y)

#values
z= thisdict.values()
print(z)

#I can also use they key value pair to add a new tuple to the dict
thisdict["genre"] = "Rich"
print(thisdict)

thisdihh = {
  "brand": "Ford",
  "model": "Mustang",
  "year": {
      
  }
}