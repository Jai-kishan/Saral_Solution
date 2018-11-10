'''
Apko ek number diya jayega manlo x toh apko 1 se leke x ke bich meh joh bi number 3 or 5 se divisible hai ushe print kardo.
Eg:
  Input: 10
  Output:
    3 5 6 9 10
'''

#Method 1
i=0
num=int(input('Enter the number:- '))
while (i<=num):
	if i%3==0 or i%5==0:
		print i,
	i+=1


#Method 2
#with the help of for loop
num=int(input('Enter the number:- '))
for i in range(num+1):
	if i%3==0 or i%5==0:
		print (i),
