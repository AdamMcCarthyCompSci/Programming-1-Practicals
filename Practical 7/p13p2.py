"""
Define max function with two variables
    If first is greater than second then
        return first
    else then
        return second
prompt for first float
prompt for second float
print result
"""
def max(a,b):
    """Function that returns the largest of its two arguments"""
    if a>b:
        return a
    else:
        return b
number1=float(input('Enter a number: '))
number2=float(input('Enter a number: '))
print('The largest of',number1,'and',number2,'is',max(number1,number2))
print('Finished!')