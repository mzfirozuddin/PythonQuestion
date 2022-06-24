s={4,5,6,7}
print(s)

s.add(10)   # add() is a method in python use to add element in set
s.add(20)
print(s)

print(len(s))   # len() is used to calculate set length

s.remove(4)  # remove 4 from set
print(s)

print(s.pop()) # remove a random element and return it
print(s)
print(s.pop())
print(s)

s1=s.union({8,11}) # return a new union set
print(s1)

s2=s.intersection({20,15,7})   #return a new intersection set
print(s2)

s.clear()       # clear the set
print(s)