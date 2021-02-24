hours = input("Enter the hours ")
pay = input("Enter the payrate ")
try:
    fhours = float(hours)
    fpay = float(pay)
except:
    print("Error, Please enter a numeric input")    
    quit()
total = 0
if fhours <= 40:
    total = fhours * fpay
else:
    extra = fhours - 40
    print(extra)
    total = (fhours-extra) * fpay
    print(total)
    total += extra * (fpay * 1.5)
print(total)    