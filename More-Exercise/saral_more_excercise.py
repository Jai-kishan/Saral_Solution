'''
1 se 1000 tak saare numbers print karne ka loop likho. Lekin

Agar number 3 se divisible hai toh "nav" print karvao.
Agar number 7 se divisible hai toh "gurukul" print karvao.
Agar number 21 se divisible hai toh "navgurukul" print karvao.
'''
i=1
while i<1000:
	if i%21==0:
		print(i,"Nav_Gurukul")
	elif i%7==0:
		print(i,"Gurukul")
	elif i%3==0:
		print(i,"Nav")
	i+=1




'''
Iss program mein hum students ki ginti aur ek student ke kharche se hisaab se pure NavGurukul ka ek mahine ka kharcha nikalenge

raw_input ka use kar ke do values ka input lo:

Number of students
Ek student ka kharcha
Iss ke hisaab se total kharcha nikalein. Agar total kharcha 50000 (50 hazar) ya usse kam hai toh print karein
 "Hum budget ke andar hain" nahi toh print karo ki hum budget ke bahar hain.
'''

Number_of_students=int(input("Enter number of student:-"))
student_ka_kharcha=int(input("Enter the budget of 1 student:-"))
expense =Number_of_students*student_ka_kharcha
if expense<=50000:
	print("Hum budget 50,000 ke andar hain")
	print("kyoki abhi hmara budget",expense,"hai")
else:
	print("hum budget 50,000 ke bahar hain")
	print("kyoki abhi hmara budget",expense,"hai")

'''
Hum iss program mein ek password checker banayenge jo yeh sunchit karega ki humara password strong hai.

Pehle user se ek password ka string input lijiye.
Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule follow karne chaiye:
Kam se kam uski length 6 honi chaiye
Jada se jada length 16 se jyada na ho
Kam se kam ek dollar ka sign ($) hona chaiye
Kam se kam password mein 2 ya 8 hona chaiye
Password mein capital A ya capital Z hona chaiye
Agar password yeh rules follow kar raha hai toh “Strong Password” print karo,
nahi toh “Weak Password” type karo
'''

user_pwd=input("Enter you password:- ")
pwd_len=len(user_pwd)
# print(pwd_len)
if pwd_len>=6 and pwd_len<=16:
	if "$" in user_pwd:
		if 2 or 8 in user_pwd:
			if "A" or "Z" in user_pwd:
				print("your password is too strong")
			else:
				print("your password is too weak")
		else:
				print("your password is too weak")
	else:
				print("your password is too weak")
else:
				print("your password is too weak")


'''
raw_input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene ke baad inn 3 mein se sabse bade number ko print karo

Note: Isme aap loops ka use nahi kar sakte.

'''
num1=int(input("Enter 1st number :- "))
num2=int(input("Enter 2nd number :-"))
num3=int(input("Enter 3rd number :-"))
if num1>num2:
	print("num-1 bada hai")
	if num3>num1:
		print ("num-3 bada hai")
		if num2>num3:
			print ("num-2 bada hai")
		else:
			print ("num-3 bada hai")
	else:
		print ("num-1 bada hai")
else:
	print ("num-2 bada hai")


'''
Ek number ka factorial 1 se leke uss number tak ke saare numbers ko ek saath multiply karke nikalta hai.

Jaise 3 ka factorial 6 hai. Kyunki 1 * 2 * 3 ko calculate karke 6 aata hai
4 ka factorial 24 hai. Kyunki 1 * 2 * 3 * 4 ko calculate karke 24 aata hai
Aise hi 7 ka factorial 5040 hai. Kyunki 1 * 2 * 3 * 4 * 5 * 6 * 7 ko calculate karke 5040 aata hai
Ab aap ek program likhoge jo ki user se ek integer input lega aur fir uska factorial print karega. Agar user 3 dalega to 6 print karega, 7 dalega toh 5040 print karega aur aise hi dusre numbers ke lie.

Note: Abhi ke liye yeh soch lo ki user sirf positive integers hi dalega. Negative integers kabhi nahi dalega.
'''
user=int(input("Enter the number :- "))
fact=1
for i in range(1,user+1):
	fact=fact*i
print(fact)

'''
#new program from more excercise
string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
Aapke code ko iss string_list se ek nayi list banani chaiye jo yeh hogi:

new_list = ["Rishabh", "Abhishek", "Divyashish"]
'''

string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
new_list=set(string_list)
print (list(new_list))


#convert into list to string
for i in new_list:
	print(i,end=" ")
print()


again_list=[]
for i in string_list:
	if i not in again_list:
		again_list.append(i)

print(again_list)


'''
Socho aapke paas 2 lists hain. Aapne aisa code likhna hain jisse ek nayi list banne jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain. Socho aapki do list yeh hain:

list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
Inn dono list se aapki nayi list yeh banni chaiye:

new_list = [1, 23, 75, 98]
Iss nayi list mein sirf 1, 75 aur 98 isliye hain kyunki aur koi bhi items dono lists mein nahi aa rahi. Dusri saari items ya toh pehli list mein aa rahi hai ya dusri mein.

Note: Aapka yeh code kitne bhi items ki list pe kaam karna chaiye. Aur dono lists ki length alag bhi ho sakti hai.

'''

list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
new_list=[]

for i in list1:
	if i in list2:
		new_list.append(i)
print (sorted(new_list))


#question-8
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new_list=[]

for i in list1:
	new_list.append(i)

for j in list2:
	if j not in new_list:
		new_list.append(j)
print(sorted(new_list))


#question-9
# Harshad numbers
user=int(input("Enter the number :- "))
new_user=list(str(user))
add=0
for i in new_user:
	add=add+int(i)
if user%add==0:
	print(add,"this is harshad number")
else:
	print(add,"this is not harshad number")

#through function
def harshad(user):
	new_user=list(str(user))
	add=0
	for i in new_user:
		add=add+int(i)
	if user%add==0:
		print (user,add,"yes this is")
	# else:
		# return (user,add,"this is not")

# user=int(input("Enter the number :- "))
# print(harshad(user))
for num in range(1,1000):
	(harshad(num))



#question=10
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [45, 10, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
for i in marks:
	max_a=i[0]
	for j in i:
		if max_a>j:
			max_a=j
	print(max_a)
#min
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [45, 10, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]

def min_a(score):
	for i in marks:
		max_a=i[0]
		for j in i:
			if max_a>j:
				max_a=j
		print(max_a)

#max
def max_a(score):
	for i in marks:
		max_a=i[0]
		for j in i:
			if max_a<j:
				max_a=j
		print(max_a)
(min_a(marks))
print("")
(max_a(marks))



#question-11
def break_into_words(user):
	user=list(sentence.split(" "))
	print(user)
sentence=input("Enter the words- ")
# sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
# break_into_words(sentence)

counter=0
while counter< len(sentence):
	print(sentence[counter])
	counter+=1