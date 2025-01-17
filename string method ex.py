#Validate user input
#username should not execeed more than 12 characters
#username must not contain spaces
#username must not contain digits

name=input("Enter your name!:")

if len(name) >12:
    print("Username not accepted it exceeds the username capacity")
elif not name.find(" ")==-1:
    print("Username must not contain space")
elif not name.isalpha():
    print("Username mustnot contain any digits")
else:
    print("logged in successfully")