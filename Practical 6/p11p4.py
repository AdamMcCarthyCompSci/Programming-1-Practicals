'''
prompt for non-negative integer
set output array with 1.0 as element within
create factorial function
        set factorial variable to 1
        for loop from 1 to a+1
            multiply factorial by counter, set as factorial
        return factorial
if limit is less than 0
    print warning
    exit
for loop from 1 to limit
    catalan variable=catalan formula, substituting i in for loop within factorial function
    add answer to output array
if input is 0
    print empty series
else
    print series
'''
limit=int(input('Enter the number of terms you want to calculate (must not be negative): '))
output=[1.0]
def factorial(a):
        factorial=1
        for counter in range(1,a+1):
            factorial*=counter
        return factorial
if limit<0:
    print('Number must be greater than or equal to 0.')
    exit()
for i in range(1,limit):
    catalan=factorial(2*i)/(factorial(i+1)*factorial(i))
    output+=[catalan]
if limit==0:
    print('Series is: []')
else:
    print('Series is:',output)