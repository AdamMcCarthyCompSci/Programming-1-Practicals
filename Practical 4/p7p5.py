'''
Set integer variable to 1 (first integer.)
Set total variable to 0.
Create while loop until integer variable goes over 10000.
    If the integer is divisible by 3 or by 5, then add it to the total.
    Add 1 to the integer variable.
    Loop repeats until integer variable goes over 10000.
Print the total.
Print finished!
'''
integer=1
total=0
while integer<=10000:
    if integer%3==0 or integer%5==0:
        total=total+integer
    integer+=1
print(total)