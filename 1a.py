#Write a Python program to accept n numbers in list and remove duplicates from a list.
def remove_duplicates(input_list):
    # Create a set from the input list to remove duplicates
    unique_list = list(set(input_list))
    return unique_list

# Ask the user for input
n = int(input("Enter the number of elements in the list: "))

# Initialize an empty list to store the numbers
input_list = []

# Loop to accept n numbers from the user
for i in range(n):
    num = int(input("Enter element {}: ".format(i + 1)))
    input_list.append(num)

# Call the function to remove duplicates
result_list = remove_duplicates(input_list)

# Display the list without duplicates
print("List with duplicates removed:", result_list)


