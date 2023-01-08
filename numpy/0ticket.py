#calculate ticket price for adult and children
#age <12 is children
#age 12 and above is adult
#age <5 is free
#adult: 5.00
#children : 2.50
import datetime
print ("Welcome to ACME Cinema")

birthYear=int(input("Insert your birth year: ").strip())
currentYear=datetime.datetime.now()
currentYear=int(currentYear.strftime("%Y"))
age=currentYear-birthYear
print(f"Your age is : {age}")

if (age<5):
    ticketPrice=0
elif (age<12):
    ticketPrice=2.50
else:
    ticketPrice=5.00

ticketPrice=format(ticketPrice,".2f")
print(f"Your ticket price is ${ticketPrice}")





    
