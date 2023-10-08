try:
    # Prompt the user for input
    num = int(input("Enter a positive integer: "))
    
    if num > 0:
        print("You entered a positive integer.")
    else:
        print("You did not enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")