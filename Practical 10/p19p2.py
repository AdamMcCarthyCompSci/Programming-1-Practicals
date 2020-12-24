"""
Define base10Conv with num and base
    make num lowercase
    make num a list
    reverse order of list num
    define letterHex with elements a-f
    power is 0
    result is 0
    for characters in num
        if char in letterHex
            char is equal to the index of the letter in letterHex plus 10
        add the integer of char times base to the power of power to result
        add 1 to power
    return result
prompt for number
prompt for base
print result, calls for base10Conv function with number and base inputs
"""
def base10Conv(num,base):
    """
    Converts a number (num) in a given base (base) to base 10

    Assumes number is in the given base format and is a string
    Assumes base is a string
    Returns result in base 10 format"""
    num=num.lower()
    num=list(num)
    num.reverse()
    letterHex=['a','b','c','d','e','f']
    power=0
    result=0
    for char in num:
        if char in letterHex:
            char=letterHex.index(char)+10
        result+=int(char)*(base**power)
        power+=1
    return result      
numberInput=str(input('Enter a number: '))
baseInput=int(input('Enter a base: '))
print(numberInput,'in base',baseInput,'is',base10Conv(numberInput,baseInput),'in base 10.')