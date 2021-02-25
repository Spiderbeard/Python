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

