#Exception Handling
try:
    innum=int(input("Insert a number: \n").strip())
    innum=innum+2
except Exception as err:
    print ("You entered invalid input")
    print ("Error: ",err)
else:
    print("Final value is: ")
    print(innum)
finally:
    print ("End")

#https://www.youtube.com/playlist?list=PLiINKPFJSaBmLlaIG3UgJ6h4ZMP-WXsCw