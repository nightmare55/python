#10 Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' ']’. These brackets must be close in the correct order. for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

class ParenthesesChecker:
    def check_validity(self, string):
        stack = []
        print(type(stack))
        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']
        for char in string:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack:         
                    return False
                if opening_brackets.index(stack[-1]) == closing_brackets.index(char):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

checker = ParenthesesChecker()

string = input("Enter a string of parentheses: ")
if checker.check_validity(string):
    print("Valid")
else:
    print("Invalid")