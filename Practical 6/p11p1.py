'''
create input variable
create factorial variable, set to 1
while input isn't negative
    prompt user for integer (neg to exit), set as input
    for loop where counter goes from 1 to input+1
        multiply factorial by counter, set as factorial
    print answer
    reset factorial variable to 1
else
    print exit statement
'''
integerinput=0
factorial=1
while integerinput>=0:
    integerinput=int(input('Enter an integer (negative integer to exit): '))
    for counter in range(1,integerinput+1):
        factorial*=counter
    print('Factorial of',integerinput,'is',factorial)
    factorial=1
else:
    print('Program exited due to negative integer input.')
print('Finished!')