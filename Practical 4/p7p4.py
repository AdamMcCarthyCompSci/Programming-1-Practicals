'''
Set integer to 1 (first integer).
Set total to 0.
Create while loop that repeats until integer variable goes over 5000.
    Add the integer to the total.
    Increase the integer by 1.
    Repeat loop until integer variable gover over 5000.
Print total.
Print finished!
'''
integer=1
total=0
while integer<=5000:
    total=total+integer
    integer+=1
print(total)
print('finished!')