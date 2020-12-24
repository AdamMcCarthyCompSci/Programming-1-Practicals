"""
Define isPalindroms with s
    define toChars with s
        s is lowercase of s
        letterString is empty string
        for loop iterating through s
            if iterator is in alphabet/0-9/space
                add iterator to letterString
        return letterString
    define isPal with s
        for loop iterating through characters in s
            if the first character of s is the same as the last
                slice the first and last characters off s
                if the length of s is less than or equal to 1
                    return true
            else
                return false
    return isPal function with toChars of s
palTest is prompt
while loop where palTest isn't empty string
    if isPalindrom with palTest
        print is palindrome
    else
        print isn't palindrome
    prompt again
print finished
"""
def isPalindrome(s):
    """Checks whether the string s is a palindrome

    Assumes s is a str.
    Returns True if the letters in s form a palindrome;
    Returns False otherwise.
    Case and non-letters are ignored."""
    def toChars(s):
        """Converts a string to lowercase and removes non-letters/numbers/spaces

        Assumes s is a str.
        Converts uppercase letters to lowercase and removes non-letters/numbers/spaces"""
        s=s.lower()
        letterString=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz0123456789 ':
                letterString+=c
        return letterString
    def isPal(s):
        """Checks whether the string s is a palindrome

        Assumes that s is a str with only lowercase letters and no non-letters
        Returns True if s is a palindrome;
        Returns False otherwise."""
        for char in s:
            if s[0]==s[-1]:
                s=s[1:-1]
                if len(s)<=1:
                    return True
            else:
                return False
    return isPal(toChars(s))
palTest=input('Enter a string (empty string to exit): ')
while palTest!='':
    if isPalindrome(palTest):
        print(palTest,'is a palindrome.')
    else:
        print(palTest,'is not a palindrome.')
    palTest=input('Enter a string (empty string to exit): ')
print('Finished!')