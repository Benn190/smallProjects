#program to output the desired number at any index in the fibonnaci sequence

def fib(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)
    
num = int(input("Enter which fibonnaci number you would like shown..."))
print(fib(num))