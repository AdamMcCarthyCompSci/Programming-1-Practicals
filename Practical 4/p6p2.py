'''
Set x as first integer inputted.
Set y as second integer inputted.
Set z as third integer inputted.
If x is greater than y and z and is not divisible by 2 (odd), then print x.
If y is greater than x and z and is not divisible by 2 (odd), then print y.
If z is greater than x and y and is not divisible by 2 (odd), then print z.
Else print none of the numbers are odd.
print finished!
'''
x=int(input('Enter first integer:'))
y=int(input('Enter second integer:'))
z=int(input('Enter third integer:'))
if x>y and x>z and x%2!=0:
    print(x)
elif y>x and y>z and y%2!=0:
    print(y)
elif z>x and z>y and z%2!=0:
    print(z)
else:
    print('None of the numbers are odd.')
print('finished!')