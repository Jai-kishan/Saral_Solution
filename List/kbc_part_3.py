question=["Ques 1: The weight of diamonds is usually measured in what?","Ques 2: Who of these politicians is this person talking about? ","Ques 3: Which state of India has the shortest coastline?","Ques 4: Vasant, Vinod, Mahasukh, Gautam and Rajesh are brothers related to whih of these business families?","Ques 5: Who is the first Indian woman wrestler to win a gold medal at the Asian Games?"]
first_option=["A. Tola","A. Mohammad Azharuddin","A. Goa","A. Hinduja","A. Sakshi Malik"]
second_option=["B. Carat","B. Kirti Azad","B. Maharashtra","B. Adani","B. Babita Kumari"]
third_option=["C. Maund","C. Imran Khan","C. Odisha","C. Ambani","C. Vinesh Phogat"]
fourth_option=["D. Troy","D. Mansoor Ali Khan Pataudi","D. West Bengal","D. Ruia","D. Kavita Devi"] 

all_option=[first_option,second_option, third_option, fourth_option]
ans_key =["B","C","A","B","C"]
correct_ans=0
question_len=len(question)

for i in range(question_len):
	print (question[i],len(question[i]))
	print(first_option[i])
	print (second_option[i])
	print(third_option[i])
	print(fourth_option[i])
	answer=str(input("Enter your answer: - "))
	if answer==ans_key[i]:
		print("Congrats")
		correct_ans+=1
		print(correct_ans)
	else:
		print("javab galat hai")


'''
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
i=0
while i<len(marks):
	print(students[i],str(marks[ i]))
	i+=1
'''