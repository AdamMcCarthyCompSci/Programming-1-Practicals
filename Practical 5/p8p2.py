'''
Prompt input
Test if input<=0
    print warning if true
else
    create variables for two multiplier numbers
    set a while loop where the loop can't exceed the inputted number
        Create nested while loop, where second variable can't exceed inputted number (other axis in table)
        multiply two variables and add space at end
        add 1 to second variable
    print empty line
    reset two variables
'''
numberinput=int(input('Enter a positive integer: '))
if numberinput<=0:
    print('Integer must be greater than 0.')
else:    
    multiplylimit=1
    multiplier=1
    while multiplylimit<=numberinput:
        while multiplier<=numberinput:
            print(multiplier*multiplylimit,end=' ')
            multiplier+=1
        print()
        multiplier=1
        multiplylimit+=1
print('Finished!')