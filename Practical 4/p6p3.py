'''
Prompt user to enter a name as a string.
If the name is Mickey Mouse or Spongebob Squarepants, then print I am not sure that is your name.
Else print you have a nice name.
Print finished.
'''
name=str(input('Enter name:'))
if name=='Mickey Mouse' or name=='Spongebob Squarepants':
    print('I am not sure that is your name.')
else:
    print('You have a nice name.')
print('finished!')