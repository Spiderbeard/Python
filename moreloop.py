total = 0
count = 0
while True:
    num = input("Enter a number ")
    
    print(num)
    if num == 'done':
         break
    try:
        newnum = int(num)
        total = total + newnum

        count = count + 1
        
    except :
        print("Invalid input")
        continue
        

print(total, count, (total/count))        