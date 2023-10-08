#Write a Python program to check if a given key already exists in a dictionary. If key exists replace with another key/value pair.
def replace_key_in_dict(input_dict, old_key, new_key, new_value):
    if old_key in input_dict:
        # Remove the old key and add the new key/value pair
        input_dict[new_key] = new_value
        del input_dict[old_key]
        print("Replaced")
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
      replace_key_in_dict(d,x,7,70)
  else:
      print('Key is not present in the dictionary')
print(d)
is_key_present(5)
print(d)
is_key_present(9)