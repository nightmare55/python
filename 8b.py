#8 Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case. Further modify the program to reverse a string word by word and print it in lower case.
class StringManipulator:
    def get_String(self):
        self.string = input("Enter a string: ")
    def print_String(self):
        print("Uppercase string:", self.string.upper())
        ls =self.string.lower()
        word = ls.split()
        rw = " ".join(reversed(word))
        print("Reversed lowercase string word by word:", rw)

g = StringManipulator()
g.get_String()
g.print_String()