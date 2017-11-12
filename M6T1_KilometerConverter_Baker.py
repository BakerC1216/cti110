# CTI-110
# M6T1 - Kilometer Converter 
# BakerC1216
# 11/12/17
# This program coverts kilometers in miles.

def AskForKilometers():
    Kilometers = float( input("Enter the distance" + \
                              "In kilometers:"))
    return Kilometers

# This line defines kilometers to miles.
def ConvertKilometersToMiles (Kilometers):
    Miles = Kilometers * 0.6214
    return Miles

def main():
    InputKilometers = AskForKilometers()
    ConvertedMiles = ConvertKilometersToMiles (InputKilometers)

    print (InputKilometers, "kilometers converted to miles is", \
           ConvertedMiles, "miles")

main()
