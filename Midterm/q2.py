'''
Create while loop.
Only break while loop when empty string entered.
Various if statements to capture days in each month using <= and >=.
Subtract inputted integer by max boundary of previous month.
Print statement.
Ask for only integers up to 365.
Print statement.
'''

dayinput=0
while dayinput!="":
    dayinput=int(input('Enter the day for which you want to find the date (an integer): '))
    print(dayinput)
    if 1<=dayinput<=30:
        print('Day number',dayinput,'is',dayinput,'September 2020')
    elif 31<=dayinput<=61:
        print('Day number',dayinput,'is',dayinput-30,'October 2020')
    elif 62<=dayinput<=91:
        print('Day number',dayinput,'is',dayinput-61,'November 2020')
    elif 92<=dayinput<=122:
        print('Day number',dayinput,'is',dayinput-91,'December 2020')
    elif 123<=dayinput<=153:
        print('Day number',dayinput,'is',dayinput-122,'January 2021')
    elif 154<=dayinput<=181:
        print('Day number',dayinput,'is',dayinput-153,'February 2021')
    elif 182<=dayinput<=212:
        print('Day number',dayinput,'is',dayinput-181,'March 2021')
    elif 213<=dayinput<=242:
        print('Day number',dayinput,'is',dayinput-212,'April 2021')
    elif 243<=dayinput<=273:
        print('Day number',dayinput,'is',dayinput-242,'May 2021')
    elif 274<=dayinput<=303:
        print('Day number',dayinput,'is',dayinput-273,'June 2021')
    elif 304<=dayinput<=334:
        print('Day number',dayinput,'is',dayinput-303,'July 2021')
    elif 335<=dayinput<=365:
        print('Day number',dayinput,'is',dayinput-334,'August 2021')
    else:
        print('Day number',dayinput,'is not in the 2020-2021 academic year!')
print('Finished!')