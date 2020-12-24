"""
Define divisors function with num1 and num2
    Divisors is tuple with 1 as element
    for loop from 2 to minimun of num1 and num2 integer divided by 2 and added by 1
        if  modulus of num1 by iterator and num2 by iterator are both 0
            add iterator to divisors tuple
    if modulus of max num by min num is 0
        add min num to divisors tuple
    return divisors tuple
prompt for number1
prompt for number2
if number1 or number 2 aren't positive
    print warning
else
    divisors is function with number1 and number2
    print result
"""
def findDivisors(num1,num2):
    """Finds the common divisors of num1 and num2

    Assumes that num1 and num2 are positive integers
    Returns a tuple containing the common divisors of num1 and num2"""
    divisors=(1,)
    for i in range(2,((min(num1,num2))//2)+1):
        if num1%i==0 and num2%i==0:
            divisors+=(i,)
    if max(num1,num2)%min(num1,num2)==0:
        divisors+=(min(num1,num2),)
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