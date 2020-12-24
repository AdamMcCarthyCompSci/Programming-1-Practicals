"""
Define function series with limit,s
    if limit is 1
        return print s
    else
        append last element in s + 2^(limit-1)
        print s
        return series function with limit-1,s
set limit as 1
while limit is greater than 0
    prompt user for number of terms
    create list with single element 1
    if limit is positive
        series function with limit,s
"""
def series(limit,s):
    """Function that returns a series of numbers according to a formula

    Assumes first argument is positive and second argument is a list
    Uses recursion
    """
    if limit==1:
        return print('Series is:',s)
    else:
        s.append(s[-1]+2**(limit-1))
        print(s)
        return series(limit-1,s)
limit=1
while limit>0:
    limit=int(input('Enter the number of terms you want to calculate (non-positive integer to exit):'))
    s=[1]
    if limit>0:
        series(limit,s)
print('Finished!')