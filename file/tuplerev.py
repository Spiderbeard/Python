Fhand = open("C:/Users/User/Desktop/p4e/file/loremipsum.txt")
counts = dict()
for line in Fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
lst = list()
for key, val in counts.items():
    newtup = (val , key)
    lst.append(newtup)
lst = sorted(lst ,reverse=True)
for val,key in lst[:10] :
    print(key, val)           


c = {'a':10, 'b':1,'c':22 }

print(sorted([ (v,k) for k,v in c.items()], reverse=True) )
