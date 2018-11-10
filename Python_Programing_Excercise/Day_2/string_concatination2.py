'''
Apko ek string di jayegi jiske akhir me agar 'ing' hogi toh ushe aage apko 'ly' add karni hai aur agar 'ing' nhi hai toh 'ing' add karna hai.
Lekin agar uske akhir meh 'ly' hai toh ushme app kuch bi add ni karoge

Eg:
  Input: 'abc'
  Output: 'abcing'

  Input: 'string'
  Output: 'stringly'
'''

string=raw_input('Enter the name:- ')
var='ing'
var2='ly'
if string[-2:]==var2:
	print string
elif string[-3:] != var:
	print string+'ing'
else:
	if string[-3:]== var:
		print string+var2
	