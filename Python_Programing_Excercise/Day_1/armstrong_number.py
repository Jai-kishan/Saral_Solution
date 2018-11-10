'''
Apko ish sawal me ek program likhna hai jishme ek value di jayegi manlo 1000 toh apko jitne bi number Armstrong Number hai 0 se 1000 ke bich me ushe print karna ha.

Eg:
  Input: 1000
  Output:
      1
    153
    370
    371
    407
'''

  
 #Armstrong Number for n series  
armstrong=int(input("Enter the Number :- "))
for i in range(armstrong):
	num=i
	result=0
	n=len(str(num))
	while i!=0:
		digit=i%10
		result=result+digit**n
		i=i//10
	if num==result:
		print num



#for now particular number is armstrong or not 
i=int(input('Enter the number '))
num=i
result=0
n=len(str(num))
while i!=0:
	digit=i%10
	result=result+digit**n
	i=i//10
if num==result:
	print 'armstrong number'
else:
	print "this is not a armstrong number "