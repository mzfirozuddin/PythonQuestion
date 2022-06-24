"""write a program to find whether a given username contains less than 10 character or not"""
username=input("Enter your username: ")
a=len(username)
if(a<10):
    print("less than 10 character")
else:
    print("more than 10 character")