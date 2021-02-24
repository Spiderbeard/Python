fhandle = open("c:/Users/User/Desktop/p4e/loremipsum.txt")
print(fhandle)
for line in fhandle:
    line = line.rstrip()
    print(line)

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened ",fname)
    quit()
for line in fhand:
    line = line.rstrip()
    print(line)            