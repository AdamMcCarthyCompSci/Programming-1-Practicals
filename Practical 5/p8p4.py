#Created program to be more modular than just the set integers and ranges
'''
Create a counter array (for analysis later)
create bracket array
set analysis to number of elements between first positive integer bracket and maximum bracket - in this case, 20,40,60,80.
create while loop where input must be >=0
    Prompt for integer (neg to exit)
    Create if statement to catch inputs=0
        add to counter for analysis
    create temp for input
    create bracket value variable
    create low bracket variable, set to 0
    create high bracket variable, set to first element in bracket array
    check and record range inside while loop, where high bracket variable must be less than final element in bracket array plus interval
        If the difference between the input and the given element in the bracket array isn't positive, then it falls into the given bracket
            print bracket statement
            record to counter
            break from loop
        if not 
            check against next element in bracket array
            add interval between ranges to low bracket
            add interval between ranges to high bracket
            reset loop
    Else statement for loop to catch numbers greater than highest bracket
        print greater than statement
        add to bracket counter
print number of inputs equal to 0
print number of inputs for first interval
create analysis variable
create while loop where analysis must not be greater than number of elements being tested
    print statement for each bracket count
print number of inputs over highers bracket
'''
numberinput=0
#variable arrays - you can change this code to be different intervals(for example, instead of ranges of 20 you can do 30), or even add more ranges by changing the three variables below (bracketcount,numberbracket,numberanalysis)
bracketcount=[0,0,0,0,0,0,0]
numberbracket=[20,40,60,80,100]
numberanalysis=3
while numberinput>=0: 
    numberinput=int(input('Enter an integer (negative integer to exit): '))
    #catch 0 input
    if numberinput==0:
        print('Number is equal to 0')
        bracketcount[0]+=1
        continue
    numbertemp=numberinput
    bracketvalue=0
    lowbracket=0
    highbracket=numberbracket[0]
    #check and record range
    while highbracket<numberbracket[-1]+(numberbracket[-1]-numberbracket[-2]): 
        if numbertemp-numberbracket[bracketvalue]<=0:
            print('Number is greater than',lowbracket,'and less than or equal to',highbracket)
            bracketcount[bracketvalue+1]+=1
            break
        else:
            bracketvalue+=1
            lowbracket+=numberbracket[-1]-numberbracket[-2]
            highbracket+=numberbracket[-1]-numberbracket[-2]
    #catch inputs above largest range
    else:
        print('Number is greater than',highbracket-(numberbracket[-1]-numberbracket[-2]))
        bracketcount[-1]+=1
bracketcount[1]-=1
#analysis
print('Equal to 0:',bracketcount[0])
print('Betweeen 0 and',numberbracket[0],':',bracketcount[1])
analysis=0
while analysis<=numberanalysis:
    print('between',numberbracket[analysis],'and',numberbracket[analysis+1],':',bracketcount[analysis])
    analysis+=1
print('Greater than',numberbracket[-1],':',bracketcount[-1])
print('Finished!')