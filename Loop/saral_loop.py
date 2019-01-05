'''
question-0
Ek flowchart banao jo 10 baar aapka naam print kare.
'''
#while loop
i=0
while i<=10:
	print(i,"\tJai-kishan")
	i+=1

#for loop

for i in range(1,11):
	print(i,"\tJai-kishan")




'''
question-1
Ek flowchart banao jo 0 se 10 tak numbers print kare.
Note:- Aapko 0 aur 10 bhi print karna hai.
'''
i=0
while i<=10:
	print(i)
	i+=1


#for loop
for i in range(0,10+1):
	print(i)




'''
question-2
Ek flowchart banao jo 11 se 45 tak saare numbers print kare.
Note:- Aapko 11 aur 45 bhi print karna hai.
'''
i=11
while i<=45:
	print(i)
	i+=1


for i in range(11,45+1):
	print(i)



'''
Question-3
Ek buiding hai jisme 10 floors hai.
Aur aap uss building ke ground floor par ho.
Aapko uss building ke top floor par jaana hai. 
Aap ek baar mein ek floor hi chadh sakte ho. 
Ground floor se top floor per jaane ka flowchart banao. 
Jab aap top par phonch jayenge tab aapko "mein top par pahunch gaya"print karna hai.
'''
i=1
while(i<=10):
	j=i
	if j==10:
		print(j,"mein top par pahunch gaya")
		break
	print(i)
	i+=1



for i in range(1,10+1):
	if i==10:
		print(i,"mein top par pahunch gaya")
		break
	print(i)

for i in range(1,10+1):
	if i==10:
		print(i,"mein top par pahunch gaya")
	else:
		print(i)

# question-4
# Ek flowchart banao jo 20 se 100 mein wahi numbers print kare jo 2 se divisible hai
# yaani numbers ka 2 se bhaag karne par remainder (shesh) 0 bachta hai.

for i in range(20,100+1):
	if i%2==0:
		print(i)


i=20
while i<=100:
	if i%2==0:
		print(i)
	i+=1



'''
question-5
Ek flowchart banao jo 1 se 100 mein wahi numbers print kare jo 7 se divisible hai yaani unka 7 se bhaag karne per remainder (shesh) 0 bachta hai.
'''
for i in range(1,101):
	if i%7==0:
		print(i)
i=1
while i<=100:
	if i %7==0:
		print(i)
	i+=1


'''
question-6
Ek flowchart banao jo 30 se 400 tak aise numbers print kare jo 3 aur 21 dono se divisible hai.
'''
i=30
while i<=400:
	if i%3==0 or i%21==0:
		print(i)
	i+=1


for i in range(30,401):
	if i%3==0 or i%21==0:
		print(i)

'''
question-7
Ek flowchart banao jo 12 se 421 tak saare numbers ka “total” calculate kare.
'''
i=12
sum=0
while i<=421:
	sum=sum+i
	i+=1
print("The sum of number is:-",sum)



sum=0
for i in range(12,422):
	sum=sum+i
print(sum)



'''
Question-8
Ek flowchart banao jo 30 se 420 tak unn numbers ka sum calculate kare
jo 8 ke multiple hai yaani wo numbers 8 ke table (paahade) mein aate hai
'''
i=30
sum=0
while i<=420:
	if i%8==0:
		sum=sum+i
	i+=1
print(sum)


add=0
for i in range(30,421):
	if i%8==0:
		add+=i
print(add)

'''
question-9
Ek flowchart banao jo 11 logon ka weight input le aur fir average weight print kare. 
Aur firr yeh bhi check kare ki kya Average weight 5 ka multiple
(yaani 5 se bhaag karne par shesh 0 bachta hai) hai ya nahi?
'''
i=1
hold=0
while i<=11:
	user=int(input("Enter your age :- "))
	hold+=user	
	i+=1
print("Total weight of 11 person is :- ",hold)
average=hold/11
print (average)
if average%5==0:
	print("5 ka multiple hai ")



add=0
for i in range(11):
	i=int(input("Enter your age:- "))
	add+=i
print(add)
average=add/11
if average%5==0:
	print("5 se divisible hai")


'''
question-10
Ek flowchart banao jo number ko neeche diye dhang se print kare.

1, -2, 3, -4, 5, -6 …99, -100
'''
for i in range(1,101):
	if i%2==0:
		print(-i,end=" ")
	else:
		print(i,end=" ")


i=0
while i<=100:
	if i%2==0:
		print(-i,end=" ")
	else:
		print(i,end=" ")
	i+=1

'''
question-11
Ab hum loops ka use karke ek game banayenge. Iss game ko hum “guessing game” bolte hai.

Iss game mein humare pass pehle se ek number hota hai. Abhi ke liye maan lo yeh number 5 hai.
Uske baad hum user se 1 se 10 ke beech mein ek number input lete hai. Phir user humare number ko guess karni ki koshish karta hai.
Jaise, agar user ne 3 input kiya. Hum check karenge ki kya 3, 5 ke barabar hai?
3, 5 ke barabar nahi hai isliye hum user se phir koi number input lenge.
Aur check karenge ki kya woh number 5 ke barabar hai?
User ko 5 chances milenge number guess karne ke liye.
Agar usne 5 chances mein number guess kar liya toh sahi hai, nahi toh ek message aa jayega ki user ne guess nahi kiya.
'''
number = 5
i=1
print("you have only 5 chances")
while i<=5:
	user=int(input("Enter the number :- "))
	if user>number:
		print("number bada hai")
	elif user<number:
		print("number chhota hai")

	if number==user:
		print("wow you are win")
		break
	i+=1
else:
	print("you are lose this game")

'''
Question-12
Ek flowchart banao jo user se 2 number input lega.
Aur fir unn number ko multiply karke print kare. Jaise,
agar input hai 5 aur 4 tab 20 print hona chahiye.

Note:- Aap * yaani ki multiply operator ka numbers ko multiply karne ke liye use nhi kar sakte. 
Aap aur kisi bhi operator (+, -) ka use kar sakte ho.
'''

#for loop
num1=int(input("Enter the 1st number :- "))
num2=int(input("Enter the 2nd number :- "))
add=0
for i in range(0,num1):
  add=add+num2

print ("The multiplication of "+ str(num1)+" and "+str(num2)+" is :-"+str(add))



num1=int(input("Enter the 1st number :- "))
num2=int(input("Enter the 2nd number :- "))
i=0
add=0
while(i<num1):
  add=add+num2
  i+=1

print(add)


'''
Question-13
Ek flowchart banao jo fibonacci series ke pehle 100 number print kare. Fibonacci series aisi hoti hai:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Iss series ka pehla_number 0 hai aur dusra_number 1 hai. Aur uske baad har number peechle do numbers ka sum hota hai.

Jaise, teesra number = pehla_number + dusra_number
1 = 0 + 1
chautha_number = dusra_number + teesra_number
2 = 1 + 1
'''

first=0
second=1
num=int(input("Enter the 1st number :- "))
for i in range(num):
  print(first)
  temp=first
  first=second
  second=second+temp