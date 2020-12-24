#Inputted value
untaxed=202046.93
print('Value to be taxed:',untaxed)
#Calculating tax ratio
lowbracket=untaxed*0.6
highbracket=untaxed*0.4
#Applying tax to initial value
lowtax=lowbracket*0.135
hightax=highbracket*0.23
total=untaxed+lowtax+hightax
print('Value after tax applied:',total)
print('Finished!')