fhand = open("c:/Users/User/Desktop/p4e/loremipsum.txt")
for line in fhand:
    line = line.upper().rstrip()
    print(line)