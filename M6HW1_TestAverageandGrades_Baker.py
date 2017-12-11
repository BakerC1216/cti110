# CTI-110
# M6HW1 - Test Averages and Grades 
# BakerC1216
# 11/12/17
# This program creates a scoring table.

def Calc_Average (Score1, Score2, Score3, Score4, Score5):
    average = (Score1 + Score2 + Score3 + Score4 + Score)/5
    return average

def Determine_Grade (Score):
    if(Score < 60):
        return "F"
    elif(Score < 70):
        return "D"
    elif(Score < 80):
        return "C"
    elif(Score < 90):
        return "B"
    elif(Score < 101):
        return "A"

def Enter_Score():
    Score1 = float( input("Please enter score 1:"))
    Score2 = float( input("Please enter score 2:"))
    Score3 = float( input("Please enter score 3:"))
    Score4 = float( input("Please enter score 4:"))
    Score5 = float( input("Please enter score 5:"))

    return Score1, Score2, Score3, Score4, Score5

def printtableofresults(Score1, Score2, Score3, Score4, Score5):
    print ("\nScore\tLetter Grade")
    print( str(Score1) + "\t\t" + Determine_Grade(Score1), \
           str(Score2) + "\t\t" + Determine_Grade(Score2), \
           str(Score3) + "\t\t" + Determine_Grade(Score3), \
           str(Score4) + "\t\t" + Determine_Grade(Score4), \
           str(Score5) + "\t\t" + Determine_Grade(Score5), sep = "\n")

def main():
    Score1, Score2, Score3, Score4, Score5 = Enter_Score()
    printtableofresults( Score1, Score2, Score3, Score4, Score5)

main()
