# CTI-110
# M2HW1 - Distance Traveled 
# BakerC1216
# 9/10/17
# Calculate the total cost of a meal
FoodCost = float (input("Enter the food cost: "))

#Calculate the tip amount as 18 percent of the food cost
TipAmount = FoodCost * .18

#Calculate the sales tax as 7 percent of the food cost
SalesTax  = FoodCost * .07

#Display the total cost
TotalCost = FoodCost + TipAmount + SalesTax
print('The TotalCost is $', format(TotalCost, ',.2f'))



