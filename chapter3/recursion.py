# imagine we want to do something like 3,2,1

def countdown(i):
    print(i)
    if i == 0:
        return
    i = i-1
    countdown(i)

countdown(5)


# Doing a recursion factorial excersise

def factorial(x):
    if x == 0 :
        return 1 
    else:
        return x * factorial(x-1)


factor_resultado = factorial(5)


print(factor_resultado)
    