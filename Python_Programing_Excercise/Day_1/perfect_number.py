'''
Apko ish sawal me ek program likhna hai jishme ek value di jayegi manlo 1000 toh apko jitne bi number Perfect Number hai 0 se 1000 ke bich me ushe print karna ha.

Eg:
  Input: 1000
  Output:
      6
     28
    496
'''

num= int(input("Enter the number for perfect number search: "))
n = 1
while n <= num:
    sum = 0
    divisor = 1
    while divisor < n:
        if n % divisor==0:
            sum += divisor
        divisor = divisor + 1
    if sum == n:
        print n, "is a perfect number"
    n = n + 1


