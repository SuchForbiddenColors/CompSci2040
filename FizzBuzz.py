#Written in Python

def FB(x):
    if(divmod(x,15)[1] == 0): #divmod returns quotient and remainder, remainder is index 1
        return "FizzBuzz"
    if(divmod(x,5)[1] == 0):
        return "Buzz"
    if(divmod(x,3)[1] == 0):
        return "Fizz"
    return x    
x = map(FB,range(1,101))
print(list(x))
