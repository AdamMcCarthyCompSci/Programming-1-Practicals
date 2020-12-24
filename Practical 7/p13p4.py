"""
Define f function with x variable
    print in statement
    add 1 to x
    set y to 1
    print x
    print y
    print z
    return x
multiple assignment x,y,z=5,10,15
print before statement
print x
print y
print z
set z to function f of x
print after statement
print x
print y
print z
"""
def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print('In function f:')
    x+=1
    y=1
    print('x is',x)
    print('y is',y)
    print('z is',z)
    return x
x,y,z=5,10,15
print('Before function f: ')
print('x is',x)
print('y is',y)
print('z is',z)
z=f(x)
print('After function f: ')
print('x is',x)
print('y is',y)
print('z is',z)
print('Finished!')