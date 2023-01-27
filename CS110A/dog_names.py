''' 
This program allows a user to input a dogs name to see if it is one of the popular names.
Inputs : name of dog
Outputs : Is it a popular dogs name
written by : Anurup 
Written date : 01/25/2023
'''

# Create a file where we input popular dog names.

file = open("dog_names.txt" , 'w')
file.write("Cooper\n")
file.write("Daisy\n")
file.write("Caesar\n")
file.write("Rocky\n")
file.write("Lilly\n")
file.close()

# Open the previously created file in read mode.
file = open("dog_names.txt" , 'r')
text = file.read()
#print(text)
# converts the file that has strings to a list of names.
text_list = text.splitlines()
file.close()
#print(text_list)

'''In case the list prints with \n
converted_list = []
for elements in text_list:
    converted_list.append(elements.replace("\n", ""))
    
print(converted_list) 
'''

# Take user input
dogs_name = input("Enter the dog's name to check if it is one of the most popular names : ")

# using try, except, finally to display the results
try:
    if dogs_name == text_list[-2]:
        print(dogs_name , "is one of the most popular dog names.")

except EOFError as e:
    print(e)

finally:
    if dogs_name != text_list[-2]:
        print(dogs_name , "is not one of the most popular dog names.")


'''
Simple python program to get used to Try, except, finally as a beginner. 
When I was working on this program \n was getting printed in the list for some reasons,
so had to create a converted list to strip the \n character. Did not need to do so but keeping it as a record,
In case I get to such problems in the future.
'''
