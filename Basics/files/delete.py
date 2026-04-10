#use the os module to delete
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#to remove a dir we use rmdir #we can only delete empty folders  