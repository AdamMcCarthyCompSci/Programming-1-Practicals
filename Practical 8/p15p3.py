"""
Define function series with limit,s
    if limit is 1
        remove last element of s from s
        return print s
    elif limit is 2
        return print s
    else
        append second last element of s + 13 x last element of s
        print s
        return series function with limit-1,s
set limit as 1
while limit is greater than or equal to 0
    prompt user for number of terms
    create list with elements 13,8
    if limit is positive
        series function with limit,s
"""
def series(limit,s):
    """Function that returns a series of numbers according to a formula

    Assumes first argument is positive and second argument is a list
    Uses recursion
    """
    if limit==1:
        s.remove(s[-1])
        return print('Series is:',s)
    elif limit==2:
        return print('Series is:',s)
    else:
        s.append(s[-2]+13*s[-1])
        print(s)
        return series(limit-1,s)
limit=1
while limit>=0:
    limit=int(input('Enter the number of terms you want to calculate (non-positive integer to exit):'))
    s=[13,8]
    if limit==0:
        print('Series is: []')
    if limit>0:
        series(limit,s)
print('Finished!')