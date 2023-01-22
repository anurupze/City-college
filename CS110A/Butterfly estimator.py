'''
Create a program that calculates butterfly population estimates
Inputs : estimated number of male butterflies, estimated number of female butterflies
Outputs : total butterflies, sex ratio, variance, gender difference, mating pairs
Written by : Anurup
Date : 01/21/2023
'''

print("Butterfly Estimator\n")

# creating variables that takes in user input for total number of male and female butterflies.
males = int(input("Enter the estimated number of male butterflies: "))
females = int(input("Enter the estimated number of female butterflies: "))

# Performing necessary calculations to get the desired outputs.

total_butterflies = males + females

sex_ratio = males / females 

# variance is the measure of spread between the numbers in a dataset
mean = (males + females) / 2
variance = (((males - mean) ** 2) + ((females - mean) ** 2)) / 2

# using the abs function so that our program doesnot return negative value.
gender_difference = abs(males - females)

# we use the min function to determine the mating pairs to ensure we donot over count the mating pairs at one go.
# even though every male and female could mate which couldve been calculated by multiplying.
mating_pairs = min(males , females)

print("\nTotal Butterflies : ", total_butterflies)

print("Sex_ratio (males : females) : " , sex_ratio)

print("variance : " , variance)

print("Gender_difference : " ,  gender_difference)

print("mating_pairs : " , mating_pairs)

'''
The variance is calculated as the average of the squared differences from the mean.
The formula for variance is (Xi - mean)^2 / n where Xi is the value of ith data point and n is the total number of data points.
In this case, we have two data points and we used the mean of these two data points as the average for variance calculation.
'''
'''
This activity is to get familiar with the math operators in python.
The operators I didnot use are the floor division operator '//', modulo operator '%'
The floor division operator rounds the result down to the nearest integer/whole number
and the modulus operator returns the remainder after division.
'''