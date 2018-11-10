'''
Pichle wale question meh app ek string di ja rahi ti jiske akhir me agar 'ing' hogi toh ushe aage apko 'ly' add karna ta ab apko 'ing' ko hata ke 'ly' add karna hai aur baki sab wese hi honge.

Eg:
  Input: 'abc'
  Output: 'abcing'

  Input: 'string'
  Output: 'strly'

'''


string=raw_input('Enter the name:- ')
var='ing'
var2='ly'

if string[-2:]==var2:
	print string
if string[-3:] == var:
	jai=string.replace([-3],"ly")
	print (jai)
elif string[-3:] != var:
	print string+'ing'
else:
	if string[-3:]== var:
		print string+var2