"""
Define isPalindroms with s
    define toChars with s
        s is lowercase of s
        letterString is empty string
        for loop iterating through s
            if iterator is in alphabet
                add iterator to letterString
        return letterString
    define isPal with s
        if length of s is less than or equal to 1
            return true
        else
            return if first element of s is the same as last element of s and call function isPal with s, except s is 1 element shorter at start and end (slice)
    return isPal function with toChars of s
palTest is prompt
while loop where palTest isn't empty string
    if isPalindrom with palTest
        print is palindrome
    else
        print isn't palindrome
    prompt again
"""
def isPalindrome(s):
    """Checks whether the string s is a palingfrome

    Assumes s is a str.
    Returns True if the letters in s form a palindrome;
    Returns False otherwise.
    Case and non-letters are ignored."""
    def toChars(s):
        """Converts a string to lowercase and removes non-letters

        Assumes s is a str.
        Converts uppercase letters to lowercase and removes non-letters"""
        s=s.lower()
        letterString=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterString+=c
        return letterString
    def isPal(s):
        """Checks whether the string s is a palindrome

        Assumes that s is a str with only lowercase letters and no non-letters
        Returns True if s is a palindrome;
        Returns False otherwise.
        Recursive function."""
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))
palTest=input('Enter a string (empty string to exit): ')
while palTest!='':
    if isPalindrome(palTest):
        print(palTest,'is a palindrome.')
    else:
        print(palTest,'is not a palindrome.')
    palTest=input('Enter a string (empty string to exit): ')
print('Finished!')