'''
Set sum variable to 0
Set input variable to 1
Create while loop where input must be greater than 0
    Prompt user for positive integer
    create for loop where counter begins at 0 and ends at input+1
        add counter to sum
    print sum
    set sum to 0
'''
integersum=0
integerinput=1
while integerinput>0:
    integerinput=int(input('Enter a positive integer (non-positive integer to end program): '))
    for counter in range(0,integerinput+1):
        integersum+=counter
    print(integersum)
    integersum=0
print('Finished!')