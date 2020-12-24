city=str(input('Enter a town or city:'))
Munster=['Cork','Limerick','Waterford']
Leinster=['Dublin','Kilkenny']
Ulster=['Belfast','Derry','Lisburn']
Connacht=['Sligo','Galway']
if city in Munster:
    print('You entered',city+'.',city,'is in Munster.')
elif city in Leinster:
    print('You entered',city+'.',city,'is in Leinster.')
elif city in Ulster:
    print('You entered',city+'.',city,'is in Ulster.')
elif city in Connacht:
    print('You entered',city+'.',city,'is in Connacht.')
else:
    print('Sorry, I didn\'t recognise that name')
print('Finished!')