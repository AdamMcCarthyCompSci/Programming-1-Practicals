"""
prompt for positive, set as limit
set x as limit
define prime function with x as first variable, and set count as 0 if not defined
    if x is 1
        if count is more than 1
            print limit and count of factors
        else
            print prime
    else
        if limit divides evenly with x-1
            set factor as limit/x-1
            print factor equation
            return prime with x-1 as first variable, and count+1 as second
        else
            return prime with x-1 as first variable and count as second
if limit is positive
    prime function of x
else
    warning
"""
limit=int(input('Enter an integer (must be >0):'))
x=limit
def prime(x,count=0):
    """Function that calculates if first argument is a prime number and lists its factors

    Assumes first argument is positive, second argument can be left blank in order to begin with the counter at 0. It counts the number of factors.
    Uses recursion
    """
    if x==1:
        if count>=1:
            print(limit,'has',count,'factors. It is not a prime number.')
        else:
            print(limit,'is a prime number.')
    else:
        if limit%(x-1)==0:
            factor=limit/(x-1)
            print((x-1),'x',factor,'=',limit)
            return prime(x-1,count+1)
        else:
            return prime(x-1,count)
if limit>0:
    prime(x)
else:
    print('Integer must be >0. The prime number sequence begins at 1.')