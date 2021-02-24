spay = input("Enter the payrate: ")
shours = input("Enter the hours worked: ")
try:
    startinghours = float(shours)
    startingpay = float(spay)
except:
   
    quit()


def payrate (startinghours, startingpay):
    
    if startinghours <= 40:
        print("Your total pay is ", startinghours * startingpay)
    else:
        overtime = startinghours - 40
        startinghours = startinghours - overtime
        pay = startinghours * startingpay
        pay += overtime * (startingpay * 1.5)   
        print("Your total pay is ", pay) 

payrate(startinghours, startingpay)