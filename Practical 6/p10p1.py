'''
Prompt for integer (neg to exit)
If integer neg
    exit
create sqaureroot variable
Create while loop where integer must be greater than squareroot^2
    add 1 to squareroot
if squareroot^2 is same as integer
    print answer
else
    print not perfect square
'''
integerinput=int(input('Enter an integer (negative number to exit):'))
if integerinput<0:
    exit()
squareroot=0
while squareroot**2<integerinput:
    squareroot+=1
if squareroot**2==integerinput:
    print('Square root of',integerinput,'is',squareroot)
else:
    print(integerinput,'is not a perfect square.')