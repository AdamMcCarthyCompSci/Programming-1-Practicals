#Entering a value
untaxed=float(input('Enter a value to be taxed:'))
print('Value to be taxed:',untaxed)
#Calculating tax ratio
lowbracket=untaxed*0.6
highbracket=untaxed*0.4
#Applying tax to initial value
lowtax=lowbracket*0.135
hightax=highbracket*0.23
totaltax=lowtax+hightax
total=untaxed+lowtax+hightax
print('Low tax:',lowtax)
print('High tax:',hightax)
print('Total tax:',totaltax)
print('Value after tax applied:',total)
print('Finished!')