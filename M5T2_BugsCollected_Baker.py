# CTI-110
# M5T2 - Bugs Collected 
# BakerC1216
# 10/22/17

# Initialize the accumulator
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    # Promp the user.
    print('Enter the bugs collected on day', day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total = total + bugs
    

# Display the toal bugs.
print('You collected a total of', total, 'bugs.')
