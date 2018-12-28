'''
Apko ish Task me input ke torh pe saal diya jayega aur apko ush saal ke 3 pichle Leap Year print karne hai.

Aur Jab 3 pichle Leap Year nikal jaye toh uske baad aap 3 ane wale Leap Year nikalne hai apko.

Eg:
  Apko ek saal di jayegi jese 1998.
  Toh apko ush saal ke piche aye hue 3 leap year nikalne hai 1996, 1992, 1988
  aur Jab nikal jaye toh apko aage ane wale 3 leap year nikalne hai 2000, 2004, 2008
'''
leap=int(input("Enter the Year for know future 3 leap year :- "))
plus=0
store=0
i=0
year=leap
print "past 3 leap year is :- ",
while leap>=i:
	if (leap%4==0 and leap%100!=0) or leap%400==0:
		store=store+1
		print leap,
		if store==3:
			break
	leap=leap-1
print ''
print "Furure 3 Leap Year is :- ",
while year>=i:
	if (leap%4==0 and leap%100!=0) or leap%400==0:
		plus=plus+1
		print year,
		if plus==3:
			break
	year=year+1

