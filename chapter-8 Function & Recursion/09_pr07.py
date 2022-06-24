def remove_and_strip(string, word):
    newStr=string.replace(word,"")
    return newStr.strip()

str1="        Firoz is a good boy     "
res=remove_and_strip(str1,"Firoz")
print(res)