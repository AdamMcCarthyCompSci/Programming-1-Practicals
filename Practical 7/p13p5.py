"""
define function f of x
    print in statement
    set v to 3
    set w to 30
    add 1 to x
    set y to 1
    set z to 20
    print v-z
    return x
multiple assignment v-z=25,20,5,10,15
print before statement
print v-z
multiple assignment w,z=f of z, f of x
print after statement
print v-z    
"""
def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print('In function f:')
    v=3
    w=30
    x+=1
    y=1
    z=20
    print('v is',v)
    print('w is',w)
    print('x is',x)
    print('y is',y)
    print('z is',z)
    return x
v,w,x,y,z=25,20,5,10,15
print('Before function f: ')
print('v is',v)
print('w is',w)
print('x is',x)
print('y is',y)
print('z is',z)
w,z=f(z),f(x)
print('After function f: ')
print('v is',v)
print('w is',w)
print('x is',x)
print('y is',y)
print('z is',z)
print('Finished!')