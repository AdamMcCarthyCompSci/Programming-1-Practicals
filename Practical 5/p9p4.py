'''
Set factorial to 1
set input to 1
set counter to 1
create while loop where input must be positive
    prompt for positive input
    create while loop where counter must not be greater than input
        multiply factorial by counter and set answer to factorial
        add 1 to counter
    if input is greater than 0
        print factorial answer
    reset factorial
    reset counter
'''
factorial=1
integerinput=1
counter=1
while integerinput>0:
    integerinput=int(input('Enter a positive integer (negative integer will end program): '))
    while counter<=integerinput:
        factorial*=counter
        counter+=1
    if integerinput>0:
        print('Factorial of',integerinput,'is',factorial)
    factorial=1
    counter=1
print('Finished!')