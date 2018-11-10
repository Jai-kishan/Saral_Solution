'''
Apko ish task meh koi bi ek number diya jayega uske piche ke 3 even number nikalo.
Jab yeh nikal jaye toh uske aage ke 3 odd number nikalo.

Eg:
  Agar number joh hai woh 10 hai
  toh uske
    Pichle 3 even number 10, 8 , 6 honge aur
    10 ke baad ane wale 3 odd number 11, 13, 15 honge

'''

#Solution
num=int(input('Enter the number :- '))
i=0
store=0
plus=0
num2=num
print "Pichle 3 Even Number is :-",
while num>=i:
	if num%2==0:
		store=store+1
		print num,
		if store==3:
			break
	num=num-1
print ""
print "Aur aage ke 3 Odd number hai :- ",
while num2>i:
	if num2%2!=0:
		plus=plus+1
		print num2,
		if plus==3:
			break
	num2=num2+1
