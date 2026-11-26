# imagine we want to do something like 3,2,1

def countdown(i):
    print(i)
    if i == 0:
        return
    i = i-1
    countdown(i)

countdown(5)