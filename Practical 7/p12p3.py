"""
Define SR function
    set tolerance to 0.01
    set step as tolerance^2
    set guesses counter to 0
    set root variable to 0.0
    while loop as long as absolute value of input-root^2 is not less than tolerance and root^2 isn't greater than input
        add step to root
        add 1 to guess counter
        Every 100000 guesses
            print number of guesses
    print number of guesses
    if absolute value of input-root^2 is less than tolerance then
        print approximate square root
    else
        print fail statement
set input as float prompt
if input isn't negative then
    SR function of input
else
    print warning
"""
def squareRoot(number):
    epsilon=0.01
    step=epsilon**2
    numGuesses=0
    root=0.0
    while abs(number-root**2)>=epsilon and root**2<=number:
        root+=step
        numGuesses+=1
        if numGuesses%100000==0:
            print('Still running. Number of guesses:',numGuesses)
    print('Number of guesses:',numGuesses)
    if abs(number-root**2)<epsilon:
        print('The approximate square root of',number,'is',root)
    else:
        print('Failed to find a square root of',number)
number=float(input('Enter a positive number (float) for which you wish to calculate the square root: '))
if number>=0:
    squareRoot(number)
else:
    print('Input must be >=0.')