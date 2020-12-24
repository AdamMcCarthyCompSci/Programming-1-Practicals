#Entering a length
length=float(input('Enter a length:'))
if length<0:
    print('Length must be >=0. Please try again.')
else:
    print('Length is:',length)
    #Calculating area of square
    areasquare=length*length
    print('Area of a square with side of this length:',areasquare)
    #Calculating volume of cube
    volumecube=length*length*length
    print('Volume of a cube with side of this length:',volumecube)
    #Calculating area of circle
    import math
    areacircle=math.pi*(length/2)**2
    print('Area of circle with diameter of this length:',areacircle)
    #Calculating volume of sphere
    volumesphere=(4/3)*math.pi*(length)**3
    print('Volume of sphere with diameter of this length:',volumesphere)
    #Calculating volume of cylinder
    volumecylinder=(math.pi)*(length)**2*(length)
    print('Volume of cylinder with diameter of this length:',volumecylinder)
print('Finished!')