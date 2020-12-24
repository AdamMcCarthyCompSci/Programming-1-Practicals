"""
Define fib function with limit,fibonacci
    if limit is 1
        remove last element of fibonacci
        return print fibonacci
    elif limit is 2
        return print fibonacci
    else
        append last element+second last element of fibonacci to fibonacci
        print fibonacci
        return fib function with limit-1,fibonacci
set limit as 1
while limit isn't less than 0
    prompt for positive integer
    fibonacci list with 0,1
    if limit is 0
        print empty series
    if limit is greater than 0
        fib function with limit,fib
"""
def fib(limit,fibonacci):
    """Function that returns the fibonacci series of numbers

    Assumes first argument is positive and second argument is a list
    Uses recursion
    """
    if limit==1:
        fibonacci.remove(fibonacci[-1])
        return print('Series is:',fibonacci)
    elif limit==2:
        return print('Series is:',fibonacci)
    else:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
        print(fibonacci)
        return fib(limit-1,fibonacci)
limit=1
while limit>=0:
    limit=int(input('Enter the number of terms you want to calculate (negative integer to exit):'))
    fibonacci=[0,1]
    if limit==0:
        print('Series is: []')
    if limit>0:
        fib(limit,fibonacci)
print('Finished!')