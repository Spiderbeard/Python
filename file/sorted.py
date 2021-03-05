fhand = open("C:/Users/User/Desktop/p4e/file/loremipsum.txt")
d = dict()
for line in fhand:
    words = line.split()
    for word in words:
        d[word] = d.get(word,0) + 1
print(sorted([(v,k) for k,v in d.items()], reverse=True))        