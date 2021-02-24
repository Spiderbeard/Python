str = "X-DSPAM-Confidence: 0.8475 "
colon = str.find(":")
num = str[colon+1:]
print(num)

newnum = float(num.strip())
newnum
print(newnum + 42)