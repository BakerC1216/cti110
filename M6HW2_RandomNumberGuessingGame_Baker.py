# CTI-110
# M6HW2 - Random Number Guessing Game 
# BakerC1216
# 11/13/17
# This program generates random number in the range of 1 through 100.

import random

def GenerateRandomNumber():
    RandomNumber = random.randint( 1, 100)
    return RandomNumber

def AskUserForNumber( Message = "Guess the number:"):
    UserNumber = int( input(Message))
    return UserNumber

def CheckUserNumber( UserNumber, RandomNumber):
    if UserNumber > RandomNumber:
        return "Too high"
    elif UserNumber < RandomNumber:
        return "Too low"
    else:
        return "Congratulations"

def main():
    UserCongratulated = False
    LetsStart = True

    while UserCongratulated or LetsStart:
        RandomNumber = GenerateRandomNumber()
        UserNumber = AskUserForNumber()
        Message = CheckUserNumber(UserNumber, RandomNumber)

        while Message != "Congratulations":
            print( Message)
            UserNumber = AskUserForNumber( "Try Again?:")
            Message = CheckUserNumber(UserNumber, RandomNumber)
    
        print( Message)
        UserCongratulated = True
    

main()
    
