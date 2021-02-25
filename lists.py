total = [40,60,80,90,100000,25,156454,654468416,65498161,944584,5198446,5849]
amount = 0
for num in total:
    amount += num
print(amount)
for i in range(len(total)):
    print(total[i])    
total.sort()
total.reverse()



print(total[1:3]) 
print(total[:4])


print(sum(total))

print(total)

numlist = list()
while True:
    inp = input("Enter a number ")
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
av = sum(numlist) / len(numlist)
print(av)    


abc = "woo:noo:boo:choo"
stuff = abc.split(':')