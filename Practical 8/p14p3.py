"""
Set count to 0
Prompt for non-negative, set as limit
if limit is negative
    print warning
    exit
for loop between 2 and limit
    if limit divides by counter evenly then
        print not prime
        break
else then
    print prime
"""
count=0
limit=int(input('Enter an an integer >=0: '))
if limit<=0:
    print(limit,'is not a prime number. The prime number sequence begins at 1.')
    exit()
for i in range(2,limit):
    if limit%i==0:
        print(limit,'is not a prime number.')
        break
else:
    print(limit,'is a prime number.')