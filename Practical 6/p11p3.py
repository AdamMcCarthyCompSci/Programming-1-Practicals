'''
set limit variable as 1
while limit isn't negative
    prompt user for integer (neg to exit)
    set first and second variables in series as 0,1 (multiple assignment)
    if limit is 0
        print series is
        continue
    else if limit is 1
        print series is first
        continue
    else if series is positive
        print series is first and second, empty sep and end
        multiple assignment, a is first and b is second
        for loop from 2 to limit
            multiple assignment where b is b+a and a is b
            print comma b, empty sep and end
        print empty
else
    print exit program
'''
limit=1
while limit>=0:
    limit=int(input('Enter the number of terms you want to calculate (negative integer to exit):'))
    f_0,f_1=0,1
    if limit==0:
        print('Series is: ')
        continue
    elif limit==1:
        print('Series is: ',f_0)
        continue
    elif limit>0:
        print('Series is: ',f_0,',',f_1,sep='',end='')
    b,a=f_1,f_0
    for i in range(2,limit):
        b,a=b+a,b
        print(',',b,sep='',end='')
    print()
else:
    print('Negative integer entered, exiting program.')
print('Finished!')
