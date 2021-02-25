fhandle = open("C:/Users/User/Desktop/p4e/loremipsum.txt")
allwords = list()
for line in fhandle:
    line = line.rstrip()
    allwords.append(line)
print(allwords)
ls = list()
for word in allwords:

    newword = word.split()
    ls.append(newword)
print(ls)
print(len(ls))
