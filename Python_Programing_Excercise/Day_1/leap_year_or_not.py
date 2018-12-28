'''
Leap Year har 4 saal me ek baar ahta hai aur woh bi ush saal me joh 4 se divisible hota hai. Lekin saat hi agar woh saal 100 se divisible hai toh ushe 400 se divisible hona padega warna woh Leap Year nhi kehlayega.

Eg:
1800 Leap Year nhi hai kyunki yeh 100 se divisible hai magar 400 se divisible nhi hai
2000 Leap Year hai kyunki yeh 100 se divisible hai aur 400 se divisible hai

'''


#Program
num=int(input('Enter the number :'))
if ((num%4==0 and num%100!=0) or num%400==0):
	print ("%d is a Leap Year"%num)
else:
	print ("%d is not a Leap Year"%num)
