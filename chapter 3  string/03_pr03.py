"""write a program to detect double space in a string and print it,  aftre that replace the double space with single space """

str="This is a string with double  space"
print(str)
doubleSpace=str.find("  ")
print(doubleSpace)

str=str.replace("  "," ")
print(str)