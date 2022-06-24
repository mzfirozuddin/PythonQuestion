# write a python script to check leap year

year=int(input("Enter a year to check leap year or not: "))

# normal if-else
"""
if year%400==0:
    print(year," is leap year.")
elif year%4==0 and year%100 !=0:
    print(year," is leap year.")
else:
    print(year," is not a leap year.")
    
 """

# if-else condition in one line
result="Leap year" if year%400==0 else "Leap year" if year%4==0 and year%100 !=0 else "Non Leap year"
print(result)
