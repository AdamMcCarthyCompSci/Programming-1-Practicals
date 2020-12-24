"""
Define divisor function with num1 and num2
    empty tuple divisors
    for loop from 1 to minimum function plus 1
        if both numbers have common divisor with modulus==0
            add this iterator to tuple
    return divisors tuple
prompt for first int
prompt for second int
if either input not positive
    print warning
else
    divisors is findDivisors function with two inputs
    print common divisors
    total is 0
    for loop iterating through divisors tuple
        add iterator to divisors
    print sum of divisors
"""
def findDivisors(num1,num2):
    """Finds the common divisors of num1 and num2

    Assumes that num1 and num2 are positive integers
    Returns a tuple containing the common divisors of num1 and num2"""
    divisors=()
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            divisors+=(i,)
    return divisors
number1=int(input('Enter a positive integer: '))
number2=int(input('Enter another positive integer: '))
if number1<=0 or number2<=0:
    print('Numbers should be >0.')
else:
    divisors=findDivisors(number1,number2)
    print('The common divisors of',number1,'and',number2,'are:',divisors)

    total=0
    for d in divisors:
        total+=d
    print('Sum of common divisors is:',total)
print('Finished')
