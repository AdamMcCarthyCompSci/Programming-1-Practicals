"""
Define perfectNumber function with x
    Define properFactors function with x
        listx is empty list
        for loop from 1 to x
            if modulus of x by divisor is 0
                append listx with divisor
            else
                return listx
    result is 0
    for loop iterating through properFactors(x) which is listx result
        add iterator to result
    if result is equal to x
        return x
numberList is empty list
num1 is integer prompt
if num1 isn't positive
    print warning
else
    for loop iterating from 1 to num1+1
        if perfectnumber function of iterator is not None
            append numberList with result
    if numberList isn't empty
        print perfect numbers
    else
        print no perfect numbers
"""
def perfectNumber(x):
    def properFactors(x):
            listx=[]
            for divisor in range(1,x):
                if x%divisor==0:
                    listx.append(divisor)
            else:
                return listx
    result=0
    for i in properFactors(x):
        result+=i
    if result==x:
        return x
numberList=[]
num1=int(input('Enter a positive integer: '))
if num1<=0:
    print('Number must be >=0.')
else:
    for i in range(1,num1+1):
        if perfectNumber(i)!=None:
            numberList.append(perfectNumber(i))
    if numberList!=[]:
        print('Perfect numbers in between 1 and ',num1,': ',numberList,sep='')
    else:
        print('No perfect numbers found in this range.')
print('Finished!')