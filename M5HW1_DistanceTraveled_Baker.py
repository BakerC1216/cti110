# CTI-110
# M5HW1 - Distance Traveled 
# BakerC1216
# 10/22/17

# Initialize the accumulator
total = 0

# Get the miles traveled for each hour.
for hour in range(1, 4):
    # Prompt the user.
    print("What is the speed of the vehicle in MPH?")
    speed = float(input("Speed: "))
    
    # Input the speed of travel.
    print("How many hours has it traveled?")
    hours = float(input("hours: "))
    
    # Add distance to total.
    distance = hour * speed
    total += distance
    

# Display the toal miles.
print('You have driven a total of', total, 'distance.')
