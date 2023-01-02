#Exception Handling

try:
    innum=int(input("Insert a number: \n").strip())
    innum=innum+2
except Exception as err:   
    #print ("You entered invalid input: ",err)
    print ("Invalid")
else:
    print("Final value is: ")
    print(innum)
finally:
    print("End")
