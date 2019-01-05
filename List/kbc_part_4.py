question=["Ques 1: The weight of diamonds is usually measured in what?","Ques 2: Who of these politicians is this person talking about? ","Ques 3: Which state of India has the shortest coastline?","Ques 4: Vasant, Vinod, Mahasukh, Gautam and Rajesh are brothers related to whih of these business families?","Ques 5: Who is the first Indian woman wrestler to win a gold medal at the Asian Games?","Ques 1: The weight of diamonds is usually measured in what?","Ques 2: Who of these politicians is this person talking about? ","Ques 3: Which state of India has the shortest coastline?","Ques 4: Vasant, Vinod, Mahasukh, Gautam and Rajesh are brothers related to whih of these business families?","Ques 5: Who is the first Indian woman wrestler to win a gold medal at the Asian Games?"]
first_option=["A. Tola","A. Mohammad Azharuddin","A. Goa","A. Hinduja","A. Sakshi Malik","A. Tola","A. Mohammad Azharuddin","A. Goa","A. Hinduja","A. Sakshi Malik"]
second_option=["B. Carat","B. Kirti Azad","B. Maharashtra","B. Adani","B. Babita Kumari","B. Carat","B. Kirti Azad","B. Maharashtra","B. Adani","B. Babita Kumari"]
third_option=["C. Maund","C. Imran Khan","C. Odisha","C. Ambani","C. Vinesh Phogat","C. Maund","C. Imran Khan","C. Odisha","C. Ambani","C. Vinesh Phogat"]
fourth_option=["D. Troy","D. Mansoor Ali Khan Pataudi","D. West Bengal","D. Ruia","D. Kavita Devi","D. Troy","D. Mansoor Ali Khan Pataudi","D. West Bengal","D. Ruia","D. Kavita Devi"] 
serial=[1,2,3,4]
all_option=[first_option,second_option, third_option, fourth_option]
ans_key =["B","C","A","B","C","B","C","A","B","C"]
price=[20000,40000,80000,160000,320000,640000,1250000,2500000,50000000,10000000]
correct_ans=0
question_len=len(question)
i=0
while i<len(question):
	print (question[i],len(question[i]))
	print(serial[0],first_option[i])
	print (serial[1],second_option[i])
	print(serial[2],third_option[i])
	print(serial[3],fourth_option[i])
	answer=str(input("Enter your answer: - "))
	if answer==ans_key[i]:
		print("Congrats")
		correct_ans+=1
		print("aapke %d sahi jawab hai"%correct_ans)
		print("aapne abhi tak",price[i],"jeeta hai \n")
	else:
		print("javab galat hai")
		break

	if i==4:
		print("Congrats aapka pehla padav paar ho chuka hai")

	elif i==7:
		print("Congrats aapka dusra padav paar ho chuka hai")

	elif i==9:
		print("Congrats caror pati ban gaye")

	i+=1


'''
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
i=0
while i<len(marks):
	print(students[i],str(marks[ i]))
	i+=1
'''