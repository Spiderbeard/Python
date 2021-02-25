fname = "C:/Users/User/Desktop/p4e/file/loremipsum.txt"
handle = open(fname)

dic = dict()
for line in handle:
    line = line.rstrip()
    line = line.strip(', .')
    #print(line) 
    wds = line.split()
    #print(wds)
    for w in wds:
       count = dic.get(w,0)
       ncount = count + 1
       dic[w] = ncount 
        

print(dic)         
 
large = -1
word = None
for k,v in dic.items():
     if v > large :
         large = v
         word = k

print(word,large)         