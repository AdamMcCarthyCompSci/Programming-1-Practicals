"""
Define fib function
    Set first two variables in series as 0,1
    if limit is 0 then
        print empty series
    else if limit 1 then
        print series with first variable
    else if limit>1 then
        print first two variables and end on same line in order to continue series
        reassign first and second variables (second as first+second, and first as second)
        print comma, second variable, end on same line
    print empty line
limit is prompted input
if limit is non-negative then
    fib function of limit
else then
    print warning
"""
def fib(limit):
    f_0,f_1=0,1
    if limit==0:
        print('Series is: ')
    elif limit==1:
        print('Series is: ',f_0)
    elif limit>1:
        print('Series is: ',f_0,',',f_1,sep='',end='')
        for i in range(2,limit):
            f_1,f_0=f_1+f_0,f_1
            print(',',f_1,sep='',end='')
        print()
limit=int(input('Enter the number of terms you want to calculate:'))
if limit>=0:
    fib(limit)
else:
    print('Number must be >=0.')
print('Finished!')
