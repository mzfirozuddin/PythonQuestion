"""
pattern print

     *
   * * *
 * * * * *

"""

n = int(input("Enter a number: "))

for i in range(n):
    print(" " * (n-i-1),end=" ")
    print("*" * (2*i+1),end=" ")
    print(" " * (n-i-1))

for i in range(1,n+1):
    print(" " * (n-i),end=" ")
    print("*" * (2*i-1),end=" ")
    print(" " * (n-i))