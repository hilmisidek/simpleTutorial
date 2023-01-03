#calculate ticket price for adult and children
#age <12 is children
#age 12 and above is adult
#age <5 is free
#adult: 5.00
#children : 2.50

import datetime
print ("Welcome to Acme Cinema.")
totalPrice=0
addTicket=True
while addTicket==True:
    age=int(input("Enter your year of birth: ").strip())
    currentYear=datetime.datetime.now()
    currentYear=int(currentYear.strftime("%Y"))
    print(currentYear)
    yourAge=currentYear-age
    print(f"Your age is {yourAge}")
    
    if (age<5):
        ticketPrice=0
    elif (age<12):
        ticketPrice=2.50
    else :
        ticketPrice=5.00

    print (f"Your ticket is : {ticketPrice}")
      
    while True:
        choice=input("1. Add another ticket\n2. Finish\nEnter your choice: ")
        if (choice=="2"):
            addTicket=False
            break
        if (choice=="1"):
            break
        if (choice !=1 or choice !=2):
            "Please enter correct number"
    totalPrice=totalPrice + ticketPrice

totalPrice=format(totalPrice,'.2f')
print (f"Your total ticket price is: ${totalPrice}")
