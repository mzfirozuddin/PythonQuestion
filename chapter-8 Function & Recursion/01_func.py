def percent(marks):     # Function Definition
    p=(sum(marks)/500)*100
    return p

marks1=[45,78,34,78,25]
petcentage1=percent(marks1)     # Function call

marks2=[25,78,80,78,66]
petcentage2=percent(marks2)     # Function call

marks3=[55,78,88,77,66]
petcentage3=percent(marks3)     # Function call


print(petcentage1,petcentage2,petcentage3)