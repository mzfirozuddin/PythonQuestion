# thislist = list(("apple", "banana", "cherry"))   # note the double round-brackets
# print(thislist)

list1 = ["apple", "banana", "cherry","apple"]
# print(list1)
[print(x) for x in list1]  # for loop in one line
print(list1.count("apple"))

list2 = [100, 20, 30, 50, 15, 35]
list2.sort()    # sort in ascending order
print(list2)


list3 = [100, 20, 30, 50, 15, 35]
list3.sort(reverse=True)    # sort in descending order
print(list3)