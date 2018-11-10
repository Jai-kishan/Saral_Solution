# num=int(input('Enter the number :- '))
# x=num%10 	#5
# y=num/10	#234

# a=y%10		#4
# b=y/10		#23

# c=b%10		#3
# d=b/10		#2
# print x+a+c+d




num=int(input('Enter the number :- '))
result=0
hold=num
while num>0:
	rem=num%10
	result=result+rem
	num=int(num/10)
print("Sum of all digits of", hold, "is: ", result)

