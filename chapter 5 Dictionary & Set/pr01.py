myDict={
    "pankha":"Fan",
    "dabba":"Box",
    "vastu":"Item",
    "kitavb":"Book"
}

print("options are: ",myDict.keys())
a=input("Enter the Hindi Words:\n")

# print("The Meaning of Your Word is: ",myDict[a])
print("The Meaning of Your Word is: ",myDict.get(a))