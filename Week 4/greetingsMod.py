def first_letter_always_uppercase(name):
    # Ensure that the first letter is uppercase and the rest is lowercase
    return name.capitalize()

input_name = input("Hello, what is your name?")

if input_name == "":
    print("Hello Stranger!")

else:
    formatted_name = first_letter_always_uppercase(input_name)
    print(f"Hello, {formatted_name}. Good to meet you!")
