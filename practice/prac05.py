fruits = ["apple","banana","orenge","pineapple","amla"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
        # newlist.append(x.upper())
    
# newlist = [x for x in fruits if "a" in x]     # above code written in one line

print(newlist)


# list1 = [x for x in range(10)]
          # or

list1 = []
for n in range(10):
    list1.append(n)

print(list1)

list2 = [x for x in range(10) if x < 5]
print(list2)


