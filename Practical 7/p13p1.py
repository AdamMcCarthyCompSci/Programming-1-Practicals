"""
Define max function with two variables
    if first is greater than second then
        return first
    else
        return second
prompt for first float, set as first variable
prompt for second float, set as second variable
biggest variable is max function of first and second variables
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
biggest=max(number1,number2)
print('The largest of',number1,'and',number2,'is',biggest)
print('Finished!')