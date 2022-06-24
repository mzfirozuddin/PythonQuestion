def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

print(maximum(7,5,2))
print(maximum(7,7,7))
print(maximum(55,100,25))
print(maximum(35,45,99))