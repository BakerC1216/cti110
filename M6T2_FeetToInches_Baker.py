# CTI-110
# M6T1 - Feet to Inches Converter 
# BakerC1216
# 11/12/17
# This program coverts feet in inches.

def AskForFeet():
    Feet = float( input("Enter the length" + \
                              " In Feet:"))
    return Feet

# This line defines feet to inches.
def ConvertFeetToInches (Feet):
    Inches = Feet * 12
    return Inches

def main():
    InputFeet = AskForFeet()
    ConvertedInches = ConvertFeetToInches (InputFeet)

    print (InputFeet, "feet converted to inches is", \
           ConvertedInches, "inches")

main()
