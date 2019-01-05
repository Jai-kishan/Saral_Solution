with open("files_question4.txt")as main_file:
	with open("Delhi.txt","w")as file1:
		with open("Shimla.txt","w") as file2:
			with open("other.txt","w") as file3:
				for i in main_file:
					if "delhi" in i:
						file1.write(i)
					elif "Shimla" in i:
						file2.write(i)
					else:
						file3.write(i)
main_file.close()



# main_file=open("files_question3.txt")
# file1=open("Delhi.txt","w")
# file2=open("Shimla.txt","w")
# file3=open("other.txt","w")
# for i in main_file:
# 	if "delhi" in i:
# 		file1.write(i)
# 	elif "shimla" in i:
# 		file2.write(i)
# 	else:
# 		file3.write(i)
# main_file.close()