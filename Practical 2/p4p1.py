#Ask the user to enter the Euro amount
euro_amount=float(input('Enter Euro amount:'))
print('Amount in Euro:',euro_amount)
#Converting Euro to US Dollars
euro_dollar_conversion=1.117547
#Converting Euro as long as the amount entered is at least zero
if euro_amount>=0:
    print('Amount in US Dollars:',euro_amount*euro_dollar_conversion)
else:
    print('Amount must be >= 0')
    print('Please try again.')
print('Finished!')