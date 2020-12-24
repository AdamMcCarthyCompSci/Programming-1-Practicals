#Entering a value
income=float(input('Enter an income to be taxed:'))
if income<0:
    print('Amount of income must be >=0. Please try again.')
else:
    print('Income to be taxed:',income)
    #Calculating tax ratio
    lowbracket=income*0.6
    highbracket=income*0.4
    #Applying tax to income
    lowtax=lowbracket*0.23
    hightax=highbracket*0.41
    totaltax=lowtax+hightax
    total=income-lowtax-hightax
    print('Low tax due:',lowtax)
    print('High tax due:',hightax)
    print('Total tax due:',totaltax)
    print('Income after tax applied:',total)
print('Finished!')