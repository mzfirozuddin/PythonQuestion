"""
pattern print

*
**
***

"""

n = int(input("Enter a number: "))

for i in range(n):
    print("*" * (i+1))

# print("\n")

for i in range(1, n+1):
    print("*" * i)