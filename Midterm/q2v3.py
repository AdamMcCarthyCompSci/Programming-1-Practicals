monthname=['September','October','November','December','January','February','March','April','May','June','July','August']
monthnumber=[30,31,30,31,31,28,31,30,31,30,31,31]
monthvalue=0
dateinput=int(input('Enter an integer: '))
dateinputprint=dateinput
if dateinput<=0:
    print('Integer must be greater than 0.')
else:
    while monthvalue<12:
        if (dateinput-monthnumber[monthvalue])<=0:
            date=dateinput
            break
        else:
            dateinput-=monthnumber[monthvalue]
            monthvalue+=1
if monthvalue<=3:
    year=2020
else:
    year=2021
print('Day',dateinputprint,'is the',date,'of',monthname[monthvalue]+',',year)