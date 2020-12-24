'''
prompt for non-negative integer, set as limit
if limit is negative
    print warning
else if limit is 0
    print series
else if limit is 1
    print series 0
else if limit is 2
    print series 0,1
else
    set first two variables in series
    print first two variables, empty sep and end
    multiple assignment where b=second factorial, a=first factorial, and counter=2
    while counter is less than limit
        multiple assignment where b=b+a, and a=b
        add 1 to counter
        print comma, b, empty sep and end
    print empty 
'''
limit=int(input('Enter the number of terms you want to calculate (must not be negative): '))
if limit<0:
    print('Number must be greater than or equal to 0.')
elif limit==0:
    print('Series is:')
elif limit==1:
    print('Series is: 0')
elif limit==2:
    print('Series is: 0, 1')
else:
    f_0,f_1=0,1
    print('Series is: ',f_0,',',f_1,sep='',end='')
    b,a,counter=f_1,f_0,2
    while counter<limit:
        b,a=b+a,b
        counter+=1
        print(',',b,sep='',end='')
    print()        
print('Finished!')
