"""
import os module
if example.html is not in path
    print warning
else
    open example.html as read format and read it, call contents pageRead
    count left bracket
    count right bracket
    if left and right brackets equal
        print balance and total pairs as left bracket
    else
        print imbalance as absolute value of left bracket minus right bracket. Total brackets are left bracket plus right bracket
    Repeat for each bracket type
"""
import os
if not os.path.isfile('example.html'):
    print('Required file (example.html) does not exist.')
else:
    pageRead=open('example.html','r').read()
    leftSideAngleBrackets=pageRead.count('<')
    rightSideAngleBrackets=pageRead.count('>')
    if leftSideAngleBrackets==rightSideAngleBrackets:
        print('Angle Brackets are balanced. Total pair(s):',leftSideAngleBrackets)
    else:
        print('There is an imbalance of',abs(leftSideAngleBrackets-rightSideAngleBrackets),'angle bracket(s). Total angle bracket(s):',leftSideAngleBrackets+rightSideAngleBrackets)
    leftSideRoundBrackets=pageRead.count('(')
    rightSideRoundBrackets=pageRead.count(')')
    if leftSideRoundBrackets==rightSideRoundBrackets:
        print('Round Brackets are balanced. Total pair(s):',leftSideRoundBrackets)
    else:
        print('There is an imbalance of',abs(leftSideRoundBrackets-rightSideRoundBrackets),'round bracket(s). Total round bracket(s):',leftSideRoundBrackets+rightSideRoundBrackets)
    leftSideCurlyBrackets=pageRead.count('{')
    rightSideCurlyBrackets=pageRead.count('}')
    if leftSideCurlyBrackets==rightSideCurlyBrackets:
        print('Curly Brackets are balanced. Total pair(s):',leftSideCurlyBrackets)
    else:
        print('There is an imbalance of',abs(leftSideCurlyBrackets-rightSideCurlyBrackets),'curly bracket(s). Total curly bracket(s):',leftSideCurlyBrackets+rightSideCurlyBrackets)
    leftSideSquareBrackets=pageRead.count('[')
    rightSideSquareBrackets=pageRead.count(']')
    if leftSideSquareBrackets==rightSideSquareBrackets:
        print('Square Brackets are balanced. Total pair(s):',leftSideSquareBrackets)
    else:
        print('There is an imbalance of',abs(leftSideSquareBrackets-rightSideSquareBrackets),'square bracket(s). Total square bracket(s):',leftSideSquareBrackets+rightSideSquareBrackets)