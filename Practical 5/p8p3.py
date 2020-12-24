'''
Prompt user for integer
Test if integer is >=0
    Print warning if true
else
    print title of times table
    create multiplier variable
    create while loop where multiplier can't exceed 20
        print multiplier, end in tab
        print multiplier*input
        add 1 to multiplier
'''
numberinput=int(input('Enter an integer (must not be negative): '))
if numberinput<0:
    print('Integer must be greater than or equal to 0.')
else:
    print('Times',numberinput,'Table')
    multiplier=0
    while multiplier<=20:
        print(multiplier,end='\t')
        print(multiplier*numberinput)
        multiplier+=1
print('Finished!')
