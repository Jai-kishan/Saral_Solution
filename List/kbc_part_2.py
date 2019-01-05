question=["Ques 1: The weight of diamonds is usually measured in what?","Ques 2: Who of these politicians is this person talking about? ","Ques 3: Which state of India has the shortest coastline?","Ques 4: Vasant, Vinod, Mahasukh, Gautam and Rajesh are brothers related to whih of these business families?","Ques 5: Who is the first Indian woman wrestler to win a gold medal at the Asian Games?"]
first_option=["A. Tola","A. Mohammad Azharuddin","A. Goa","A. Hinduja","A. Sakshi Malik"]
second_option=["B. Carat","B. Kirti Azad","B. Maharashtra","B. Adani","B. Babita Kumari"]
third_option=["C. Maund","C. Imran Khan","C. Odisha","C. Ambani","C. Vinesh Phogat"]
fourth_option=["D. Troy","D. Mansoor Ali Khan Pataudi","D. West Bengal","D. Ruia","D. Kavita Devi"] 

all_option=[first_option,second_option, third_option, fourth_option]
ans_key =["B","C","A","B","C"]

# question_list variable ko use kar ke second question ko use karo.
print (question[1])


# first_options, second_options, third_options, fourth_options ka use kar pehle question ki chaaron options ko print karo.
print (first_option[1])
print (second_option[1])
print (third_option[1])
print (fourth_option[1])



# Ab all_options waali lsit ka use kar ke third question ki saari options ka print karo.
print(all_option[0][2])
print(all_option[1][2])
print(all_option[2][2])
print(all_option[3][2])

# pop function use karke questions_list mein se last question aur chaaron, first_options, second_options, third_options, fourth_options mein se uski saari options ko delete karo.
question.pop()
print (question)
first_option.pop()
print(first_option)


# questions_list ki length print karo
print(len(question))



# append function use kar ke questions_list mein ek naya question aur first_options, second_options, third_options, fourth_options mein uski ek ek option add karo.
question.append("Ques 9: Who holds the Guinness Wole Record for the oldest person to be elected for the first time as PM of a nation?")
print(question)

first_option.append("A. P V Narasimha Rao")
second_option.append("B. Chaudhary Charan Singh")
third_option.append("C. Morarji Desai")
fourth_option.append("D. H D Deve Gowda")

print(first_option)
print(second_option)
print(third_option)
print(fourth_option)


# second_options waali list ke second element ko ek second_option naam ke variable mein store kar ke print karo.
option2=second_option[1]
print(option2)

print(option2 in third_option)