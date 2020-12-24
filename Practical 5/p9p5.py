'''
set first input to possible
if possible less than 0
    print warning
else
    set first factorial to 1
    create for loop where counter starts at 1 and ends at possible+1
        multiply first factorial by counter, set answer as first factorial
same code to find factorial of offered variable
if possible-offered is less than 0
    print warning
else
    find factorial of possible-offered (same as above)
Use probability formula from practical sheet
print answer
'''
possible=int(input('Enter the number of possible toppings: '))
if possible<=0:
    print('Possible toppings must be greater than 0.')
    exit()
else:
    possiblefactorial=1
    for counter in range(1,possible+1):
        possiblefactorial*=counter
offered=int(input('Enter the number of toppings offered: '))
if offered<=0:
    print('Toppings offered must be greater than 0.')
    exit()
else:
    offeredfactorial=1
    for counter in range(1,offered+1):
        offeredfactorial*=counter

if possible-offered<0:
    print('There must be more possible toppings than the amount offered.')
else:
    possibleofferedfactorial=1
    for counter in range(1,possible-offered+1):
        possibleofferedfactorial*=counter
    combinations=possiblefactorial/(offeredfactorial*possibleofferedfactorial)
    print('The number of combinations of',possible,'toppings from',offered,'possible toppings is',combinations)