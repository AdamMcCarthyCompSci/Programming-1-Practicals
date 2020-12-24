"""
Define divisors function with num1
    Divisors is tuple with 1 as element
    for loop from 2 to num1 integer divided by 2 and added by 1
        if  modulus of num1 by iterator is 0
            add iterator to divisors tuple
    add num1 to divisors tuple
    return divisors tuple
prompt for number1
if number1 isn't positive
    print warning
else
    divisors is function with number1
    print result
"""
def findDivisors(num1):
    """Finds the divisors of num1

    Assumes that num1 is a positive integer
    Returns a tuple containing the common divisors of num1"""
    divisors=(1,)
    for i in range(2,(num1//2)+1):
        if num1%i==0:
            divisors+=(i,)
    divisors+=(num1,)
    return divisors
number1=int(input('Enter a positive integer: '))
if number1<=0:
    print('Number should be >0.')
else:
    divisors=findDivisors(number1)
    print('The divisors of',number1,'are:',divisors)
print('Finished')