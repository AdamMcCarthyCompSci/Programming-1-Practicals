'''
Create vowels array (both cases)
create input variable
create count variable
while input isn't empty
    prompt user to enter string (empty to exit), set input as input variable
    for loop to iterate through characters in input
        if character is in vowel array
            add 1 to count
    print vowel count
    reset vowel count
'''
vowels=['a','e','i','o','u','A','E','I','O','U']
stringinput=0
vowelcount=0
while stringinput!='':
    stringinput=input('Enter a string(empty string to exit)')
    for characters in stringinput:
        if characters in vowels:
            vowelcount+=1
    print(stringinput,'vowel count:',vowelcount)
    vowelcount=0