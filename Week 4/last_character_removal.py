def remove_last_character(input_string):
    # Check if the string has one or fewer characters
    if len(input_string) <= 1:
        return input_string
    else:
        # Return the string with the last character removed
        return input_string[:-1]

# Test the function
input_str = input("Enter a string: ")
result = remove_last_character(input_str)

print("Original String:", input_str)
print("String with Last Character Removed:", result)
