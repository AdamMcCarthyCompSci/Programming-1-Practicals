'''
Ask the user to enter a year. Set the variable year as the user input (it must be an integer).
If the year is greater than zero, then continue the calculation.
    If the year is not divisible by 4, then print that the year is not a leap year.
    Else if the year is not divisible by 100, then print that the year is a leap year.
    Else if the year is not divisible by 400, then print that the year is not a leap year.
    Else print that the year is a leap year.
Else print that the year must be greater than 0.
'''
#Using the Wikipedia algorithm.
year=int(input('Enter a year:'))
if year>0:
    if year%4!=0:
        print('Year is not a leap year.')
    elif year%100!=0:
        print('Year is a leap year.')
    elif year%400!=0:
        print('Year is not a leap year.')
    else:
        print('Year is a leap year.')
else:
    print('The year must be greater than 0.')
print('finished!')