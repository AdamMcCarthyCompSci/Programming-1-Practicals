'''
Set integer variable to 1 (first variable).
Create a while loop that repeats until the integer variable goes over 50.
    Print the integer.
    Square the integer and set it as a new variable, 'integersquared'.
    print this squared integer.
    Add 1 to to the integer variable.
    Repeat this loop until the integer variable goes over 50.
Print finished!
'''
integer=1
while integer<=50:
    print('Integer:',integer)
    integersquared=integer**2
    print('Integer Squared:',integersquared)
    integer+=1
print('finished!')