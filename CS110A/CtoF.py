'''
This program displays the celsius tempratures and their Fahrenheit equivalents.
Inputs : None
Outputs : Celsius temprature and their fahrenheit equivalents.
written by : Anurup 
Date : 1/24/2023
'''

# Column Headers.
print("\t Celsius     Fahrenheit" )

# Dashes to match with the output.
print("\t _ _ _ _ _ _ _ _ _ _ _ _ \n ")

# Using a for loop to iterate through the range of the temprature
for c in range(-20, 19, 2):

    # Calculation to print the fahrenheit values.
    f = 9 * c / 5 + 32

    # Print statement with required decimal count after the number.
    print(" %13.0F %13.1F "  %(c , f))


print("\t _ _ _ _ _ _ _ _ _ _ _ _ \n ")

'''
The print statement with modulus are the format specifiers.
This program doesnot take any input and outputs the fahrenheit equivalents of celsius readings.
'''