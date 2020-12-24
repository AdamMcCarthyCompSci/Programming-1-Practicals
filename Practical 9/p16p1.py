"""
define series function with arguments limit and s
    if limit is 1
        print base case info
        return print series is s
    else
        append formula result
        print recursion info
        return recursive function
limit is 1
while limit is greater than or equal to 1
    limit is integer input
    s is list with element 2
    if limit is greater than 0
        call series function with limita and s
"""
def series(limit,s):
    """Function that returns a series of numbers according to a formula

    Assumes first argument is positive and second argument is a list
    Uses recursion
    """
    if limit==1:
        print('Returning base case')
        return print('Series is:',s)
    else:
        s.append(2*s[-1])
        print('appending a new element:',s[-1])
        return series(limit-1,s)
limit=1
while limit>=1:
    limit=int(input('Enter the number of terms you want to calculate (non-positive integer to exit):'))
    s=[2]
    if limit>0:
        series(limit,s)
print('Finished!')