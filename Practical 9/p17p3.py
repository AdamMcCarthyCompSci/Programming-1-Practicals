"""
stringInput is prompt for string
counter is lowercase stringInput
cat is count of string cat in counter
dog is count of string dog in counter
if cat equals dog
    print same number
else
    print not same number
"""
stringInput=input('Enter a string: ')
counter=stringInput.lower()
cat=counter.count('cat')
dog=counter.count('dog')
if cat==dog:
    print('Cat and dog appear the same number of times.')
else:
    print('Cat and dog do not appear the same number of times.')