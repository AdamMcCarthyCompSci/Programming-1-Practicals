'''
Prompt for positive integer
if input isn't positive
    print warning
else
    set factorial variable to 1
    create for loop where counter starts at 1 and ends at input+1
        multiply factorial variable by counter
    print factorial answer
'''
integerinput=int(input('Enter an integer to calculate its factorial (must be positive): '))
if integerinput<=0:
    print('Integer must be greater than 0.')
else:
    factorial=1
    for counter in range(1,integerinput+1):
        factorial*=counter
    print('Factorial of',integerinput,'is',factorial)
    print('Finished!')