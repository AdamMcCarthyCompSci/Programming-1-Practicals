"""
Define function xyz with a
    import regex
    a is a list of times where xyz appears in the string, but not preceded by '.'. Added a catch for when xyz is at the beginning of the string
    if length of a isn't 0
        return true
    else
        return false
prompt user for input
print function call of xyz with input
"""
def xyz(a):
    """
    Says whether xyz appears in string, but it can't be preceded by a '.'

    Assumes a is a string
    Returns true if xyz appears and isn't preceded by '.'
    Returns false otherwise"""
    import re
    a=re.findall('[^+.]xyz|\Axyz',a)
    if len(a)!=0:
        return True
    else:
        return False
strA=input('Enter a string: ')
print(xyz(strA))