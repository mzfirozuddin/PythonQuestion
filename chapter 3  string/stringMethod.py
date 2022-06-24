mystr="firoz is a good boy"
str="hello"
str2="hello123"
str3="hello bro"
print(type(mystr))

print(mystr.isalnum())  # Check if all the characters in the text are alphanumeric
   # alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
    #Example of characters that are not alphanumeric: (space)!#%&? etc.

print(str.isalnum())

print(mystr.isalpha())  #Check if all the characters in the text are letters
print(str.isalpha()) 
print(str2.isalpha()) 

print(mystr.endswith("boy"))      #it check this string ends with "boy" or not
print(str.endswith("boy"))

print(mystr.count("o"))     # "o" letter present 4 times in mystr string

print(len(mystr))   # calculate string length

print(mystr.capitalize())  # convert first character in capital letter

print(mystr.find("is"))   # it is use to find any word or char present in string or not
print(mystr.find("g"))     #if present then return index no
print(mystr.find("l"))     # in not present then return -1

print(mystr.upper())      # convert this string to upper case
print(mystr.lower())      # convert this string to lower case

print(str3)
print(str3.replace("bro", "guys"))   #replace "bro" with "guys"

print(str+" "+str2)     # concate str and str2

