#if
x=int(input("Insert x value: ").strip())
y=int(input("Insert y value: ").strip())

print (f"x value is {x}, y value is {y}")
if (x<y):
    print ("x<2 is true")
else:
    print ("x<2 is false")
if (x>y):
    print ("x>2 is true")
else:
    print ("x>2 if false")
if (x==y):
    print ("x==2 is true")
else:
    print ("x==2 is false")

#grading
#0-10 : fail
#11-20 : pass
#21-30 : excellent

mark=int(input("Insert your mark: ").strip())
if (mark<11):
    print("You fail")
elif (mark<21):
    print("You pass")
else:
    print ("You are excellent")


#https://www.youtube.com/playlist?list=PLiINKPFJSaBmLlaIG3UgJ6h4ZMP-WXsCw


