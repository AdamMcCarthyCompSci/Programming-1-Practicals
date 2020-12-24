"""
Define pal function with s
    result is s
    while length of s is greater than 1
        if first element of s is the same as last
            slice off first and last elements of s
        else
            return not palindrome
    else
        return is palindrome
prompt for input
while input isn't empty
    run pal function
    prompt for input
"""
def isPal(s):
    """Checks whether the string s is a palindrome

    Assumes that s is a str with only lowercase letters and no non-letters
    Prints if s is a palindrome;
    Prints fail statement otherwise."""
    palResult=s
    while len(s)>1:
        if s[0]==s[-1]:
            s=s[1:-1]
        else:
            return print(palResult,'is not a palindrome.')
    else:
        return print(palResult,'is a palindrome')
palTest=input('Enter a string with lower-case letters (empty string to exit): ')
while palTest!='':
    isPal(palTest)
    palTest=input('Enter a string with lowercase letters (empty string to exit): ')
print('Finished!')