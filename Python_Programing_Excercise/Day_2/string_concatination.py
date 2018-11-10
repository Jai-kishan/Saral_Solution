'''
Apko ek string di jayegi jahan apko string ke phele 2 aur akhir ke 2 letters print karwana hai lekin agar woh string meh 2 se kaam letters hai toh kuch bi nhi print hoga.

Eg:
  Input: 'string'
  Output:'stng'
'''

string=raw_input('Enter the name:-')
print string[0:2]+string[-2:]