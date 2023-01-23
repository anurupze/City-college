'''
This program allows the user to enter the amount of butterflies and displays the total amount collected in a day.
Inputs : number of butterflies collected each day.
Outputs : Total butterflies collected.
Written by : Anurup
Date : 01/22/2023 
'''

# Introductory line
print("WELCOME TO THE BUTTERFLY COLLECTING PROGRAM.")

# Introductions for the user.
print("\nPlease enter the amount of butterflies collected each time spent in the field.")
print("Please enter -1 when finished.\n")

butterflies = 0
total = 0

# Take the user's input.
butterflies = int(input("How many butterflies were you able to collect? or (input -1 to exit) : "))

# using a while loop with sentinel value to exit / break out of the loop.
while butterflies != -1:
    total += butterflies
    butterflies = int(input("How many butterflies were you able to collect? or (input -1 to exit) : "))

print("\nHERE IS THE TOTAL NUMBER OF BUTTERFLIES YOU COLLECTED FOR THE DAY.")
print("Total Butterflies collected :" , total)

'''
This is a simple program that returns the total number of butterflies collected in a single day.
We used a while loop to record the number of butterflies collected by the person throught the day.
It takes a sentinel value to break out of the while loop,
unless the user enters the sentinel value it asks them to enter the number of butterflies collected
so the user can collect the butterflies and come back anytime to record the number.
'''