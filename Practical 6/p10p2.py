'''
Prompt for integer (0 to exit)
If integer equals 0
    exit
create cuberoot variable
while cuberoot^3 is less than absolute value of integer
    add 1 to cuberoot
if cuberoot^3 equals absolute value of integer
        if integer is less than 0
            change cuberoot to positive
        print answer
else
    print not perfect cube
'''
integerinput=int(input('Enter an integer (0 to exit):'))
if integerinput==0:
    exit()
cuberoot=0
while cuberoot**3<abs(integerinput):
    cuberoot+=1
if cuberoot**3==abs(integerinput):
    if integerinput<0:
        cuberoot=-cuberoot
    print('Cube root of',integerinput,'is',cuberoot)
else:
    print(integerinput,'is not a perfect cube.')