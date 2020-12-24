"""
define factorial function of variable x
    if x is 0 then
        return 1
    else then
        print x
        return x multiplied by factorial function of x-1
prompt for non-negative integer
if input isn't negative
    print factorial function of input
else then
    print warning
"""
def fact(x):
    """Function that returns the factorial of its argument
    Assumes that its argument is a non-negative integer
    Uses a recursive definition
    """
    if x==0:
        return 1
    else:
        print(x)
        return x*fact(x-1)
        
number=int(input('Enter an integer (must be >=0): '))
if number>=0:
    print(fact(number))
else:
    print('Integer must be >=0.')