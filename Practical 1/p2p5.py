#Demonstrating slices of indexes
#String of animals
alphabet='A','B','C','D','E'
#Example segment of the first three letters
seg=alphabet[0:3]
print('Segment is:',seg)
#When x and y are the same
print('(a)')
seg=alphabet[0:0]
print('Segment is:',seg)
#When x is greater than y
print('(b)')
seg=alphabet[1:0]
print('Segment is:',seg)
#When x is omitted
print('(c)')
seg=alphabet[:5]
print('Segment is:',seg)
seg=alphabet[:0]
print('Segment is:',seg)
#When y is omitted
print('(d)')
seg=alphabet[0:]
print('Segment is:',seg)
seg=alphabet[5:]
print('Segment is:',seg)
#When both x and y are omitted
print('(e)')
seg=alphabet[:]
print('Segment is:',seg)