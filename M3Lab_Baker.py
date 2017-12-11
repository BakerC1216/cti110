# CTI-110
# M3Lab 
# BakerC1216
# 9/24/17
# Baker

# I was supposed to put a comment here
# My Last Name

def main():
# This program takes a number grade and outputs a letter grade.

# system uses 10-point grading scale
    A_score = 90
# TO DO: define the rest of the scores

    
score = int(input('Enter score: '))

if score >= 90:
    print('Your grade is: A')

if score >= 80:
     print('Your grade is: B')

if score <= 59:
    print('Your grade is: F')
    print('Study, and try again.')
else:
    print('You have passed')
    
# program start
main()
