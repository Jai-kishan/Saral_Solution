'''
question-1
Code likho jo iss list mein se maximum dhund kar ke print kare.

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
Aapke program ka output 70 hona chaiye.
'''
#through max function
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
print (max(numbers))

#without useing max function
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
lst=numbers[0]
store=0
for i in numbers:
  if i>lst:
    lst=i

print(lst)


'''
Code likho jo neeche di gayi lists ke items ko reverse order yaani ki ulta print kare.

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
Aapke code ka outut yeh hona chaiye:

delhi
gujrat
rajasthan
punjab
kerela
'''	
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# for i in places:
#   print(i)
for i in places:
  print (i)


'''
Palindrome wo strings ya numbers hote hai jo ulta seedhe same hote hai. Jaise, NITIN. Nitin ko aap left se padho ya right se, nitin hi hai. Aise hi MOM bhi ek palindrome hai.

Code likho jo check kare ki kya list palindrome hai ya nahi. Aur print karo “Haan! palindrome hai” agar hai. Aur “nahi! Palindrome nahi hai” agar nahi hai.

Abhi ke liye iss list ko use kar ke code likh sakte ho:

name=[ ‘n’, ’i’, ‘t’, ‘i’ , ‘n’ ]
'''
# name=['n','i','t','i','n']
name=['a','b','c','d','e']
rev=name[::-1]
# print (rev[0])
# print(rev)
if name== rev:
  print("Palindrome hai")
else:
  print("Palindrome nhi h ")

#list example
student_marks = [23, 45, 89, 90, 56, 80] 
length= len(student_marks)
print(length)
index=0
calc=0
while index<length:
  calc+=student_marks[index]
  index+=1
print(calc)

#list_example -2
student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87,9]
length =len(student_marks)
low=0
heigh=0
index=0
while index<length:
  marks=student_marks[index]
  if marks<50:
    low = low+1
  else:
    heigh=heigh+1
  index+=1

print(heigh)
print(low)