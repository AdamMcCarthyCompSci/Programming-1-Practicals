"""
define codestring function with x
    x is the count of 'code' in x
    return count
prompt for string input
call codestring function with input
"""
def codeString(x):
    """
    counts how many times 'code' appears in string (case-sensitive)
    
    assumes x is string
    returns count in string"""
    x=x.count('code')
    return print('"code" count in string:',x)
stringInput=input('Enter a string: ')
codeString(stringInput)
