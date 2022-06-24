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

b={ }      # its a empty dictionary
print(b)

print(a)   # print dictionary

print(a["fast"])   # access dictionary element
print(a["firoz"])
print(a["marks"])
print(a["anotherdict"])

print(a["anotherdict"]["neha"])     # access inner dictionary element

a["marks"]=[99,95,78]   # update dictionary value
print(a["marks"])

print(a["marks"][2]) # access "marks" 3rd index value which is present in dictionary   

