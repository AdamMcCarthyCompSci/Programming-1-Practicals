'''
Set the password as a string variable storedpasswords.
Ask the user to input a string with the statement 'Enter password:'. Set this as the variable enteredpassword.
If enteredpassword is the same as storedpassword, then print successful login.
Else print wrong password, enter correct password three times.
    Set correct variable to 0.
    Create while loop where correct must be less than 3.
        Prompt user to enter password, set this string as enteredpassword.
        If enteredpassword is the same as storedpassword, then add 1 to correct.
            If correct is equal to 3, then print successful login.
        else print denied access and break from whole loop.
Print finished!
'''
storedpassword='hunter2'
enteredpassword=str(input('Enter password:'))
if enteredpassword==storedpassword:
    print('You have successfully logged in.')
else:
    print('Sorry, the password is wrong. Please enter the correct password three times.')
    correct=0
    while correct<3:
        enteredpassword=str(input('Enter password:'))
        if enteredpassword==storedpassword:
            correct+=1
            if correct==3:
                print('You have successfully logged in.')
        else:
            print('You have been denied access.')
            break
print('finished!')