f = open("hello.txt", "r")   #filepath and instruction
print(f.read())  #the read() takes as parameter the number of characters we want to read read(5)
f.close()  #always close files when you are done with them