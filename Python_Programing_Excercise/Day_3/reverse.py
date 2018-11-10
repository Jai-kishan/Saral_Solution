# num=int(input('Enter the number :- '))
# string=str(num)
# print string[::-1]



# def reverse_number(n):
#     r = 0
#     while n > 0:
#         r *= 10
#         r += n % 10
#         n /= 10
#     return r

# print(reverse_number(123))


num=int(input('Enter the number :- '))
result = 0
while num > 0:
    result =result* 10
    result =result+ num % 10
    num =num/10

print result