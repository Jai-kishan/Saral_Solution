num=int(input('Enter the number :- '))
power=int(input('Enter the number of Power:- '))
total= num**power 
result=0
hold=total
while total>0:
	rem=total%10
	result=result+rem
	total=int(total/10)
print (num,"ka power",hold,"hai aur power",hold,"ka sum",result,"hai")
