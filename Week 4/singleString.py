def count_upper_and_lower_letters(sin_str):
    """Returns the number of uppercase letters and lowercase letters in the string."""
    upper_count = 0
    lower_count = 0

    for char in sin_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count


input_string = input("Enter a string: ")

upper_count, lower_count = count_upper_and_lower_letters(input_string)

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
