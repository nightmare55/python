# 9 Write a Python script using class to reverse a string word by word.
def reverse_words(input_str):
    words = input_str.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

input_string = input("Enter a string: ")
reversed_string = reverse_words(input_string)
print("Original String:", input_string)
print("Reversed String:", reversed_string)
