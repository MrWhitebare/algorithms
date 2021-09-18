def factorial(num:int):
    if(num<=0):
        return 1
    else:
        return num*factorial(num-1)

num=factorial(6)
print(num)