'''
#Question-1

Ek number naam ke variable mein ek variable input lo aur usko integer mein type cast kar lo.
Agar yeh number 10 se chota hai tab print karo “10 se chota hai”. 
Agar wo 10 se bada hai aur 20 se chota hai tab print karo “20 se chota hai”.
 Aur agar 20 se bada hai tab print karo ki “20 se bada hai”. 
Iss information ka use kar kar flowchart complete karo.
'''
number =int(input("Enter the number :- "))
if number<10:
	print ("10 se chota hai")
elif number>=10 and number<20:
	print ("20 se chota hai")
else:
	print ("20 se bada hai ")






'''
question-2
Aapke paas ek variable hai, jisme yeh value hai:

varx = 300 - 123
Ek flowchart banao jo user se ek number input le. Fir uss number ko integer mein convert kar ke check kare ki woh number varx ke barabar hai ya nahi.

Agar barabar hai toh print karo barabar hai nahi toh print karo barabar nahi hai.
'''

varx = 300 - 123
number = int(input("Enter the number  :- "))
if number == varx:
	print("Number barabar hai")
else:
	print("Number barabar nhi hai")






'''
Question-3
Aapke paas ek variable hai, jisme yeh value hai:

number = 44 * 30
Ek flowchart banao jo user se ek alag number input le aur dekhe ki user ne jo number daala hai,
 woh number variable ke number is bada hai ya barabar hai.

Agar bada ya barabar hai toh print karo ki number, 
bada ya barabar hai nahi toh print karo chota hai. Pehla iska flowchart banao,
aur fir code likh ke bhi submit karo
'''

number = 44 * 30
user = int(input("Enter the number :- "))
if user== number:
	print("Number barabar hai")
else:
	print("Number barabar nhi hai")




'''
Question-4
Agar water filter mein paani 1L se kam hai to aur paani bharna hai.
Agar paani 1L se 10L ke beech mein hai to aur nahi bharna.
Aur agar 10L se jyada hai to paani overflow kar jata hai.
Neeche diye flowchart ko iss information ka use karke complete karo.

Paani ke level ke liye aap user se ek water naam ke variable mein input lo, aur fir usko integer mein convert kar lo.
'''
water = int(input("Enter the water level:- "))
if water <=1:
	print ("paani bharna hai")
elif water >1 and water<10:
	print("paani nhi bhrna hai ")
else:
	print("paani overflow ho raha hai")



'''
question-5
User se ek varx naam ka variable input lo.
Usko integer mein convert karo.
Check karo ki yeh number 2 se divisible hai ya nahi.
'''
varx=input("Enter the number :-")
varx =int(varx)
print (type(varx))

if varx %2 ==0:
	print("ye 2 se divisible hai")
else:
	print("divisible nhi hai")


'''
Question-6
Use se do numbers varx aur vary naam ke variables mein input lo.
Fir yeh check karo ki kya varx vary se divisble hai ya nahi.
'''
varx=int(input("Enter the first number :- "))
vary=int(input("Enter the second number :- "))

if varx % vary==0:
	print("ye 2 se divisible hai")
else:
	print("divisible nhi hai")


'''
question-7
Ek flowchart banao jo user se 2 numbers input le. Aur dono mein se bade number ko print kare.
'''
varx=int(input("Enter the first number :- "))
vary=int(input("Enter the second number :- "))
if varx >vary:
	print("pehla number bada hai",varx)
else:
	print("dusra number bada hai",vary)




'''
question-8
Ek flowchart banao jo user se ek number input 
le aur yeh check kare ki kya number 5 aur 15 dono se divisible hai?
'''

num=int(input("Enter the number :- "))
if num%5==0 or num%15==0:
	print ("divisible hai")
else:
	print("divisible nhi hai")



'''
question-9
Socho aap ek planet par ho jahan yeh rules hain
5 saal ki umar ke baad school ja sakte ho.
18 saal ki umar ke baad vote de sakte ho.
21 saal ki umar ke baad car drive kar sakte ho.
24 saal ki umar ke baad shaadi kar sakte ho.
25 saal ke baad legally drink kar sakte ho.

Ab ek flowchart banao jo user se uski “age” input le. Aur print kare ki wo inme se kya kya cheezein kar sakta hai. Jaise agar usne age 20 daali toh woh print karega

Aap school ja sakte ho
Aap vote daal sakte ho
Agar usne age 24 daali toh print karega:

Aap school ja sakte ho
Aap vote daal sakte ho
Aap car drive kar sakte ho
Aap shaadi kar sakte ho
'''

age=int(input("Enter your age :- "))
if age>=5:
	print ("Aap school ja sakte ho")

if age>=18:
	print("Aap vote daal sakte ho")

if age >=21:
	print ("Aap car drive kar sakte ho")

if age>=24:
	print("Aap shaadi kar sakte ho")

if age >=25:
	print("aap drink kar skte hai")