
def ask_question():
	print("Who is the founder of Facebook?")
	option=["Mark Zuckerberg","Bill Gates","Steve Jobs","Larry Page"]
	for i in option:
		print(i)

ask_question()


i=0
while i<100:
	ask_question()
	i+=1


def say_hello(name):
    print ("Hello ", name)
    print ("Aap kaise ho?")
say_hello("jai")




def add_number(num1,num2):
	print("hum2 numbers ko add krenge")
	print(num1+num2)

add_number(112,3)
varx=10
vary=20
add_number(varx,vary)



def say_lang(name,language):
	if language=="punjabi":
		print("sat sri akaal",name)
	elif language=="hindi":
		print("Namestye",name)
	elif language=="English":
		print("good morning",name)

say_lang("rishabh","hindi")
say_lang("jai","English")



def print_lines(name,position):
	print("mera naam "+str(name)+" hai")
	print("mein "+str(position)+" ka co-founder hu")

print_lines("jai","Navgurkul")




def add_numbers(number1,number2):
	add=number1+number2
	print(number1,"aur",number2," ka sum:-",add)

add_numbers(56,12)

num1=[15,20,30]
num2=[20,30,40]
def add_num_list(num1,num2):
	i=0
	b = []
	while i<len(num1):
		add = num1[i]+num2[i]
		i+=1
		b.append(add)
	return (b)

print(add_num_list(num1,num2))






num1=[15,20,30,2, 6, 18, 10, 3, 75]
num2=[20,30,40,6, 19, 24, 12, 3, 87]
def add_num_list(num1,num2):
	i=0
	while i<len(num1):
		if num1[i]%2==0 and num2[i]%2==0:
			print("even hai")
		else:
			print("odd hai")
		i+=1
(add_num_list(num1,num2))





def add_numbers_print(number_x, number_y):
    number_sum = number_x + number_y
    return number_sum
sum4 = add_numbers_print(4, 5)
print (sum4)
print (type(sum4))



def calculator(numx,numy,operator):
	if operator=="add":
		add=numx+numy
		return add
	elif operator=="subtract":
		subtract=numx-numy
		return subtract
	elif operator=="multiply":
		multiply=numx*numy
		return multiply
	elif operator=="divide":
		divide=numx/numy
		return divide

num1=int(input("Enter the 1st number :- "))
num2=int(input("Enter the 2nd number :- "))
num3=input("which action you want to perform (add/subtract/multiply/divide)")
print(calculator(num1,num2,num3))



a=[3,4,5,6]
b=[2,4,5,6]
def list_change(a,b):
	i=0
	multiply=0
	c=[]
	while i<len(a):
		multiply=a[i]*b[i]
		c.append(multiply)
		i+=1
	return c
print(list_change(a,b))
