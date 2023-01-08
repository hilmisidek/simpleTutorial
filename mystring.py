#string
myString="red,apple"
newString=myString.split(",")
print(newString)
print(newString[0])
upString=newString[0].upper()
print(upString)
lowString=upString.lower()
print (lowString)
listStr=list(newString[0])
print(listStr)
listStr.reverse()
print(listStr)
finalStr=""
for lim in listStr:
    finalStr=finalStr+lim
print (finalStr)