num=int(input('Enter the number :- '))
first=0
second=1
for i in range(num-1):
	print (first)
	temp=first
	first=second
	second=second+temp