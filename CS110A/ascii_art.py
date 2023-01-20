'''
This program produces simple output.
Outputs : An ASCII art of a Dog looking through the telescope.
Author : Anurup
Date : 01/19/2023
'''

# Displays in the console 
print("Here is my console output \n")

# Creates an external text file and opens it. 'w' opens the file with write mode.
file = open("ascii_out.txt" , 'w')

# .write helps us to write in the external file without us ever having to go to the external file
file.write("A doggo looking through a telescope \n")
file.write("     .-.                  \n")                               
file.write("    {}``; (|=======|     \n")                            
file.write("    / ('    / | \         \n")                              
file.write("(  /  |    /  |  \        \n")                             
file.write(" \(_)_]]  /   |   \       \n")
file.write("Why cant I see a thing hooman?\n" + "Please human help me I would like to see the stars.")
file.write("\nFooled you Doggo I closed the eye piece.")

# Always close a file once you have opened it.
file.close()

# opens the text file we created in read mode(r)
file = open("ascii_out.txt", 'r')
text = file.read()
# prints the text file on to the console.
print(text)
file.close()

print("The doggo was never able to view the stars because of his evil Hooman.")

'''
This activity was to get familiar with python and to create an external file using python and ascii art.
It is a simple program but helps us understand how to create steps to get desired output.
'''