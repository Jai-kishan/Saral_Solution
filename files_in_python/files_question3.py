'''
Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki file mein nayi line mein daalo. Aapki list yeh rahi:

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]

'''
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
my_file=open("files_question3.txt","w")
for i in banks_list:
	my_file.write(i+"\n")
my_file.close