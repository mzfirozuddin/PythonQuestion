"""Write a program to print the content of a list using while loop"""

fruits = ["Banana","Watermelon","Grapes","Mangoes"]
i=0
# print using while loop
while i<len(fruits):
    print(fruits[i])
    i=i+1
print("\n")
# print using for loop
for item in fruits:
    print(item)