bag = dict()
bag["laptop"] = "hp"
bag["tablet"] = "samsung"
bag["cat"] = "meow"
print(bag)
print(bag["cat"])
bag["cat"] = "meow meow"
print(bag)
newdic = { 'time': 1, "lot" : 2 , "bob" : 6}

count = dict()
names =["tim","mike","tim","bob","mike","bob","tim"]
for name in names:
    count[name] = count.get(name,0) + 1
print(count)            


