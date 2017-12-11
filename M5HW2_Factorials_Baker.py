# CTI-110
# M5HW3 - Factorials
# BakerC1216
# 10/22/17

#Find the factorial of a nonnegative integer.

#Prompt the user.
integer = int(input("Enter a nonnegative integer"))
factorial = 1

for number in range(1, integer + 1):
    factorial *= number

#Display the factorial.
print("The factorial of", integer, "is", factorial)
    
