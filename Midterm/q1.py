'''
Ask for integer.
If integer less than 0, print statement.
Else: while loop using inputted integer to capture modulus of 3,5,7,11.
Count up by 1 if true.
Add 1 to while loop.
'''
integerinput=int(input('Enter an integer:'))
print('You entered: ',integerinput)
if integerinput<0:
    print('Number entered should be >=0')
else:
    count=1
    divisible3=0
    divisible5=0
    divisible7=0
    divisible11=0
    while count<=integerinput:
        if count%3==0:
            divisible3+=1
        if count%5==0:
            divisible5+=1
        if count%7==0:
            divisible7+=1
        if count%11==0:
            divisible11+=1
        count+=1
    print('Number of numbers divisible by 3: ',divisible3)
    print('Number of numbers divisible by 5: ',divisible5)
    print('Number of numbers divisible by 7: ',divisible7)
    print('Number of numbers divisible by 11: ',divisible11)
print('Finished!')