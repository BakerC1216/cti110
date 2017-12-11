# CTI-110
# M3HW2 - Software Sales
# BakerC1216
# 9/24/17

def main():
# This program takes an age and ouputs an age group.


    Quantity_100 = 40
    
quantity = int(input('Enter quantity: '))

if quantity >= 100:
    print('Your discount is: 40%')

elif quantity >= 50:
    print('Your discount is: 30%')

elif quantity >= 20:
    print('Your discount is: 20%')

elif quantity >= 10:
    print('Your discount is: 10%')

elif quantity <= 9:
    print('Your discount is: 0%')
    
# program start
main()
