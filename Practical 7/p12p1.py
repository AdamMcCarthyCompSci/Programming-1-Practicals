"""
Define function
    set fact variable=1
    for loop, starting at 1 and ending in a+1
        Multiply fact by counter each iteration
    return fact
prompt user for non-negative, set as input variable
if input>=0 then
    print factorial function of input
else then
    print warning
"""
def factorial(a):
    factorial=1
    for i in range(1,a+1):
        factorial*=i
    return factorial
integerinput=int(input('Enter a non-negative integer: '))
if integerinput>=0:
    print(factorial(integerinput))
else:
    print('Integer must be >=0.')
print('Finished!')