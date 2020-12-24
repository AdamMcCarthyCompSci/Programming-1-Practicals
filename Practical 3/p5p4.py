EnteredInteger=int(input('Enter an integer:'))
if EnteredInteger==0:
    print('The integer is equal to 0')
elif 0<EnteredInteger<=20:
    print('The integer is greater than 0, and less than or equal to 20.')
elif 20<EnteredInteger<=40:
    print('The integer is greater than 20, and less than or equal to 40.')
elif 40<EnteredInteger<=60:
    print('The integer is greater than 40, and less than or equal to 60.')
elif 60<EnteredInteger<=80:
    print('The integer is greater than 60, and less than or equal to 80.')
elif 80<EnteredInteger<=100:
    print('The integer is greater than 80, and less than or equal to 100.')
elif 100<EnteredInteger:
    print('The integer is greater than 100.')
else:
    print('The integer is negative.')
print('Finished!')