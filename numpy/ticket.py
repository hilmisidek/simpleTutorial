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
adult=0
children=0
baby=0
age=-1
while addTicket==True:
    while (age<0):
        birthYear=int(input("Enter your year of birth: ").strip())
        currentYear=datetime.datetime.now()
        currentYear=int(currentYear.strftime("%Y"))
        age=currentYear-birthYear
        if (age<0):
            print("Please enter valid year of birth")
    
    print(f"Your age is {age}")
    if (age<5):
        ticketPrice=0
        baby=baby+1
    elif (age<12):
        ticketPrice=2.50
        children=children+1
    else :
        ticketPrice=5.00
        adult=adult+1

    print (f"Your ticket is : {ticketPrice}")
    
    #while repeat will always run until break
    repeat=True
    while repeat==True:
        choice=input("1. Add another ticket\n2. Finish\nEnter your choice: ")
        if (choice=="2"):
            addTicket=False
            repeat=False
        elif (choice=="1"):
            age=-1
            repeat=False
        elif (choice !=1 or choice !=2):
            print("Please enter correct number")
    
    totalPrice=totalPrice + ticketPrice

totalPrice=format(totalPrice,'.2f')
print("Ticket breakdown:")
print(f"Adult :{adult}. Total adult price=${format(adult*5.00,'.2f')}")
print(f"Children :{children}. Total childen price=${format(children*2.50,'.2f')}")
print (f"Your total ticket price is: ${totalPrice}")
