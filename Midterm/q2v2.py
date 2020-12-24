monthname=['September','October','November','December','January','February','March','April','May','June','July','August']
monthnumber=[30,61,91,122,153,181,212,242,273,303,334,365]
monthvalue=0
dateinput=int(input('Enter an integer: '))
if dateinput<=0:
    print('Integer must be greater than 0.')
elif dateinput<=30:
        date=dateinput
else:
    while monthvalue<12:
        if (dateinput-monthnumber[monthvalue])<=0:
            date=dateinput-monthnumber[monthvalue-1]
            break
        else:
            monthvalue+=1
if monthvalue<=3:
    year=2020
else:
    year=2021
print('Day',dateinput,'is the',date,'of',monthname[monthvalue]+',',year)