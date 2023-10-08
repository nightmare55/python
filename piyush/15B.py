def remove_odd_index_characters(string):
  new_string = ""
  for i in range(len(string)):
    if i % 2 == 0:
      new_string += string[i]
  return new_string
string = input("Enter a string: ")
new_string = remove_odd_index_characters(string)
print("The new string is:", new_string)
