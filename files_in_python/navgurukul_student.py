student_name=['jai','saquib','nitin','shiv nath','shakru','apoorv']
with open("navgurukul_student.html","w") as student_file:
	student_file.write("<html> \n<head> \n<title> NG_Students_Name</title> \n</head> \n<body> \n")
	student_file.write("<ul>\n")
	for i in student_name:
		student_file.write("<li> "+ i + "</li>\n")
	student_file.write("</ul> \n</body> \n</html>\n")
	student_file.close()