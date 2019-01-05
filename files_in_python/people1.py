#how to open files
my_files=open("people1.txt")
files=my_files.read()
print(files)
my_files.close()

#method-2
# with open("people1.txt","r") as file:
# 	print(file.read())
# 	file.close()












# with open("people1.txt", "r") as file:
#     data = file.readlines() 
#     for line in data: 
#         word = line.split() 
#         print (word) 