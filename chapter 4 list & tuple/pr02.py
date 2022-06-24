"""write a program to accept marks of 6 students and display them in a stored manner"""

m1=input("Enter 1st student marks: ")
m2=input("Enter 2nd student marks: ")
m3=input("Enter 3rd student marks: ")
m4=input("Enter 4th student marks: ")
m5=input("Enter 5th student marks: ")
m6=input("Enter 6th student marks: ")

myList=[m1,m2,m3,m4,m5,m6]

myList.sort()
print(myList)
