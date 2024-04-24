def count_letters_digits(input_string):
    # Initialize counts for letters and digits
    num_letters = 0
    num_digits = 0
    
    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            num_letters += 1
        # Check if the character is a digit
        elif char.isdigit():
            num_digits += 1
    
    # Print the counts
    print("Letters:", num_letters)
    print("Digits:", num_digits)

# Input from the user
user_input = input("Enter a string: ")

# Call the function with the user input
count_letters_digits(user_input)
