# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.  Sample String: 'The quick Brown Fox'  Expected Output:  No. of Upper case characters: 3  No. of Lower case characters: 13
def count_case_characters(input_string):
    # Initialize counters for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1
    
    # Print the results
    print("No. of Upper case characters:", uppercase_count)
    print("No. of Lower case characters:", lowercase_count)

# Ask the user for input
user_input = input("Enter a string: ")

# Call the function with the user's input
count_case_characters(user_input)