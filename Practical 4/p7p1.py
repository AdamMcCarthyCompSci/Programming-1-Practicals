'''
Ask for the user to enter a year, it must be an integer. Set this input as the variable year.
If the year is greater than zero, then continue with the calculations.
    If the year is divisible by 4 and not divisible by 100, OR if the year is divisible by 100, then print the year is a leap year.
    Else print that the year is not a leap year.
Else, print that the year must be greater than zero.
Print finished!
'''
#Using algorithm from Lecture 8.
year=int(input('Enter a year:'))
if year>0:
    if (year%4==0 and year%100!=0) or year%400==0:
        print('Year is a leap year')
    else:
        print('Year is not a leap year')
else:
    print('The year must be greater than 0.')
print('finished!')