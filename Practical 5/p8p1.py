'''
set input variable to 0
create while loop where number inputted must be negative to exit
set empty string to prepare final print statement
If statements where input is tested for even division
    If true, then add string of divisible number, and additional comma string
Additional if statement to cover numbers that don't have even divisions
    reset loop with continue
Last if statement prints the input and its even divisors (remove last string which is comma)
'''
numberinput=0
while numberinput>=0:
    numberinput=int(input('Enter a series of integers (enter a negative number to exit): '))
    divisiblenumbers=''
    if numberinput%2==0:
        divisiblenumbers+='2'','
    if numberinput%3==0:
        divisiblenumbers+='3'','
    if numberinput%5==0:
        divisiblenumbers+='5'','
    if numberinput%7==0:
        divisiblenumbers+='7'','
    if divisiblenumbers=='' and numberinput>=0:
        print('This number is not divisible by 2, 3, 5, or 7')
        continue
    if numberinput>=0:
        print(numberinput,'is divisible by:',divisiblenumbers[:-1])
print('Finished!')