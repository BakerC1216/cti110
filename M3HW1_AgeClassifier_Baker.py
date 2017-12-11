# CTI-110
# M3HW1 - Age Classifier
# BakerC1216
# 9/24/17


def main():
# This program takes an age and ouputs an age group.


    Adult_age = 20
    
age = int(input('Enter age: '))

if age <= 1:
    print('You are an: Infant')

elif age <= 12:
    print('You are a: Child')

elif age <= 19:
    print('You are a: Teenager')

if age >= 20:
    print('You are an: Adult')
    
# program start
main()
