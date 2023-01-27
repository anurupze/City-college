'''
This program creates a pie chart of monthly expenses
Inputs: none
Outputs: pie chart with monthly expenses
Written by: Anurup 
Written date: 01/06/2023
'''
# Import Module for plotting
import matplotlib.pyplot as plt

# Creates a text file that has montly expenses written on it.
file = open("monthly_expenses.txt", 'w')
file.write("1000\n")
file.write("250\n")
file.write("350\n")
file.write("200\n")
file.write("375\n")
file.write("800\n")
file.close()

# opens the file to read.
file = open("monthly_expenses.txt", 'r')
read = file.read()

# creates a list and splits it.
read_lines = read.splitlines()
file.close()

# Pie chart, where the slices will be ordered and plotted Counter-clockwise.
labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Transportation', 'Misc']

# the values from the text file are used to plot the chart
values = read_lines

# creating the pie chart
plt.pie(values , labels=labels)
plt.title("Monthly Expenses")
plt.show()

'''
simple python program that gives us an overview on how to create graphs using python. 
In this case pie chart.
'''