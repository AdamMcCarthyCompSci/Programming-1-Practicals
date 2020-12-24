"""
Define codeString function with x
    import regex function
    x is a list of all appearances of code in x, where the d in code can be any letter
    return count
prompt for input
call codeString function with input
"""
def codeString(x):
    """
    counts how many times code (case-sensitive) is in string, but the d can be any letter of the alphabet.
    
    Assumes input is a string
    Returns count"""
    import re
    x=re.findall('co[a-z]e',x)
    return print('"code" count in string:',len(x))
stringInput=input('Enter a string: ')
codeString(stringInput)