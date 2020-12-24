"""
Define base function with num,conv,rem as a blank,and baseResult as an empty list
    if num is 0
        strResult is empty string
        for i in reversed baseResult
            add string i to strResult
        return strResult as an int
    else
        append modulus of num and conv to baseresult
        return base function call with num integer divided by conv, conv, modulus of num and conv, and baseResult
Prompt for base 10 number
Prompt for base to convert to
print result
"""
def base(num,conv,rem=0,baseResult=[]):
    """
    Converts 'num' to base 'conv'.

    Assumes num and conv are positive ints
    rem is the remained of the modulus of num and conv, default is 0
    baseresult is empty list that will be filled via recursion
    returns result in int format"""
    if num==0:
        strResult=''
        for i in baseResult[::-1]:
            strResult+=str(i)
        return int(strResult)
    else:
        baseResult.append(num%conv)
        return base(num//conv,conv,num%conv,baseResult)
base10=int(input('Enter a number in base 10 (positive int): '))
baseConvert=int(input('Enter the base you want to convert to (up to base 10 and positive int): '))
if base10<1 or baseConvert<1:
    print('Number and base must both be positive integers.')
else:    
    print(base10,'in base',baseConvert,'is',base(base10,baseConvert))