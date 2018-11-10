user_input =raw_input('Enter the paragraph: -')
string=str(user_input)
a = ["*",":",".","!",",","&"," ",'']
new_string = ""

for i in string:
   if i not in a:
      new_string += i
   else:
      new_string = new_string  + " "

print(len(new_string.split(" ")))