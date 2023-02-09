'''
This Program displays if the date entered by the user is a magic date or not.
Inputs: Date, Month, Year
Outputs: Is a magic date, Is not a magic date.
written by: Anurup
Written Date: 02/09/2023
'''

# program starts here
print("Magic Date's \n")

# Takes the users input of month day and the year they were born.
month = int(input(" Enter the month you were born in? "))

day = int(input("\n Enter the day of the month were you born in? "))

year = int(input("\n Enter the last two digits of the year you were born in? "))

# 
if year == month * day:
    print("\nIt's a magical date.")
else:
    print("\nSorry. Thats just a regular date ... not magic")

'''
This program creates a simple output that notifies the user if their birth date is a magical date or not.
the basic conception is if their birth month multiplied with their birth date is equal to the year they were born its a magical date.
Note: everyone is born in a magical date since to be born is a magic on its own. 
'''
