a={
    "fast":"In a quick manner",
    "firoz":"A coder",
    "marks":[56,25,66],
    "anotherdict":{      # dictionary in a dictionary
        "harry":"A daccer",
        "neha":"A singer"
    },
    1:50
}

print(a)

print(a.keys())  #print the keys of dictionary
print(list(a.keys()))  # first typecast in list then print the keys of dictionary

print(a.values())  #print the values of dictionary

print(a.items())    #print the (key,value) for all content of the dictionary

newDict={

    "lovis":"friend",
    "diviya":"friend",
    "subham":"A player",
    "firoz":"hacker"
}

a.update(newDict)

print(a)

print(a.get("fast"))
print(a["anotherdict"].get("harry"))
print(a.get("abc"))     #if not match with any key then return None

# difference between .get() and [] syntax in dictionary

print(a.get("firoz2"))  # return None if "firoz2" is not present in dictionary

#print(a["firoz2"])  # throws an error if "firoz2" is not present in dictionary