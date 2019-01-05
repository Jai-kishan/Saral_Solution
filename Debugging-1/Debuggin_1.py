'''
question-1
print "We will learn debugging by removing all the errors from this python file.
'''
print ("We will learn debugging by removing all the errors from this python file.")



'''
question-2
year = 2016
name = "NavGurukul"
print name + ', ' +   + "mein start hua tha!"

'''
year = 2016
name = "NavGurukul"
print (name + ', ' + str(year) + " mein start hua tha!")



'''
question-3
price_milk = raw_input("1L milk ka price daalo?")
print "10L milk " + price_milk*10 + " rupees ka aata hai."
'''
price_milk = int(raw_input("1L milk ka price daalo?"))
print ("10L milk " + str(price_milk*10) + " rupees ka aata hai.")


'''
Question-4
number = raw_input("please enter a decimal number")
print "your number divided by 2 is equal to = " + number/2
'''
number = float(raw_input("please enter a decimal number "))
print ("your number divided by 2 is equal to = " + str(number/2))


'''
Question-5
#Tumhare paas 5 mangoes hai
mangoes = 5
# Kisi ne humhe 5 aur mangoes de diye
manGoes = mangoes + 5
# Ab tumne unn mangoes ko 5 logo mei baant diya
print mangoes / 5
# Par isse toh 1 mango hi mila. Par milne 2 chahiye the.
Code ko sahi karo jisse ki sabko sahi mangoes mile.
'''

#Tumhare paas 5 mangoes hai
mangoes = 5
# Kisi ne humhe 5 aur mangoes de diye
manGoes = mangoes + 5
# Ab tumne unn mangoes ko 5 logo mei baant diya
print manGoes / 5
# Par isse toh 1 mango hi mila. Par milne 2 chahiye the.
Code ko sahi karo jisse ki sabko sahi mangoes mile.




'''
Question-6
# Aapke paas ek variable mein `raw_input` se gaadi ki speed ka ek integer hai
speed = int( raw_input("Gaadi ki speed daalo > ") )

# Ab aapne speed check kar ke kuch print karna hai:
# Agar 60 se kam hai toh print karna: "Speed kam hai"
# Agar 30 se kam hai toh print karna: "Speed bahot kam hai"
# Agar 100 se zyada hai toh print karo: "Bahot zyada hai"
if speed < 60:
    print "Speed kam hai"
elif speed < 30:
    print "Speed bahot kam hai"
elif speed > 100:
    print "Speed bahot fast hai"

# Isme ek baar speed 20 daal ke dekho aur dekho ki "Speed bahot kam" hai ki
# output aati hai ya nahi. Agar nahi aati toh isko theek karo aur yeh socho
# ki kya problemn hai.
'''
speed = int( raw_input("Gaadi ki speed daalo > "))
if speed <= 30:
    print "Speed bahot kam hai"
elif speed>30 and speed <= 60:
    print "Speed kam hai"
elif speed >=100:
    print "Speed bahot fast hai"



'''
question-7
# `raw_input` ka use kar ke user se din aur abhi ka samay (lunch, dinner) input
# leke uss samay ka menu print karvana hai. Abhi hum sirf monday aur tuesday ke
# liye likh rahe hain
# Monday aur Tuesday dono time daal roti banegi, bas Tuesday raat ko Pav Bhaji banegi
# Neeche waale program mein jab tuesday daalte ho toh pav bhaji print nahi hota.
# Isko sahi karo.
day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")
time = raw_input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "monday" or day == "tuesday":
    print "Daal-Roti banegi aaj"
elif day == "tuesday" and time == "dinner":
    print "Pav-Bhaji banegi aaj toh :)"w

'''
day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")
time = raw_input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "tuesday" and time == "dinner":
    print "Pav-Bhaji banegi aaj toh :)"
elif day=="monday" or day=="tuesday" or day=="tueday" and time=="lunch":
    print "Daal-Roti banegi aaj"