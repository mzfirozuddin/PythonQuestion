def factorial(n):
    if n==1 or n==0:      # Base condition
        return 1
    
    return n*factorial(n-1)     # Recursion Call

print(factorial(5))
print(factorial(4))