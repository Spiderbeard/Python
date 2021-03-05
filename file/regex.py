import re
hand = open("C:/Users/User/Desktop/p4e/file/loremipsum.txt")
for line in hand:
    line = line.rstrip()
    if re.search('dolore',line):
        print(line)