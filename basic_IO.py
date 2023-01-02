#to print
print ("hello world")

#to get input from user
myinput = input ("Message prompt: ")

#to print variable
print (myinput)

#to print text and variable in single line
myinput = input ("Message prompt: ")
print(f"Your input is {myinput}")


#to create a file and close it
f=open("simpleTutorial.txt","x")
f.close()

#to write a file in overwrite mode
f=open("simpleTutorial.txt","w")
f.write("I write this file using python")
f.close()

#to write a file in append mode
f=open("simpleTutorial.txt","a")
f.write("\nThis is the next line")
f.close()

#https://www.youtube.com/playlist?list=PLiINKPFJSaBmLlaIG3UgJ6h4ZMP-WXsCw