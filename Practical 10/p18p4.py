"""
Define endString function with a,b
    a is made lowercase
    b is made lowercase
    if a ends with b or vice versa
        return true
    else
        return false
prompt for first string
prompt for second string
print function call of first and second prompts
"""
def endString(a,b):
    """
    Says whether either string ends with the other one

    Assumes two string inputs
    Returns true if a ends with b or vice versa
    Returns false otherwise"""
    a=a.lower()
    b=b.lower()
    if a.endswith(b) or b.endswith(a):
        return True
    else:
        return False
strA=input('Enter a string: ')
strB=input('Enter another string: ')
print(endString(strA,strB))