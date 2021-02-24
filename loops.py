cont = input("Enter y to continue n to exit ")
while cont == "y" :
    print("Continue")
    cont = input("Enter y to continue n to exit ")
while True:
    line = input("> ")
    if line == 'n':
        break
    if line[0] == '#':
        continue
            