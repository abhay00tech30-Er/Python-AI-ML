"""Practice Question 3 
Write a program that: 
● Takes a sentence as input 
● Converts it to lowercase 
● Replaces all spaces " " with underscores "_" 
● Prints the new string"""
takeInpu = input("Enter Your Sentence : ")

# Convert to lowercase
lower_str = takeInpu.lower()

# Replace spaces with underscores
new_str = lower_str.replace(" ", "_")

# Print the result
print(new_str)
