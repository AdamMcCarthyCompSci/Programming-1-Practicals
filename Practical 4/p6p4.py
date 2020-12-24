'''
Set storedpassword variable as string.
Set attempts equal to 0.
Start while loop where attempts must be less than or equal to 3.
    Prompt user to enter a password string. Set this input as enteredpassword.
    If enteredpassword is the same as storedpassword, then print successful login and break from loop.
    Else add 1 to attempts.
Once user tries more than 3 times to enter the password unsuccessfully, then print denied access.
Print finished!

'''
storedpassword='hunter2'
attempts=0
while attempts<=3:
    enteredpassword=str(input('Enter password:'))
    if enteredpassword==storedpassword:
        print('You have successfully logged in.')
        break
    else:
        attempts+=1
else:
    print('You have been denied access.')
print('finished!')