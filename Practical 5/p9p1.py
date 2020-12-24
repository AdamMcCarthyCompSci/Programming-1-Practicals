'''
Prompt for positive integer
If input isn't positive
    print warning
else
    set counter variable
    set sum variable
    create while loop where counter must not be greater than input
        add counter to sum
        add 1 to counter
    print sum
'''
integerinput=int(input('Enter a positive integer: '))
if integerinput<=0:
    print('Integer must be greater than 0.')
else:
    counter=0
    integersum=0
    while counter<=integerinput:
        integersum+=counter
        counter+=1
    print(integersum)
print('Finished!')