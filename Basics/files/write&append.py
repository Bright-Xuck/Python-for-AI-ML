f = open("hello.txt", "a")
print(f.write("added new text to the bottom of the file"))
f.close()

f = open("hello.txt", "r")
print(f.read())
f.close