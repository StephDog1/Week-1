password = input("Input password:")
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

if len(password) < 8:
    print("Password must be over 8 characters.")
    exit(0)

elif len(password) > 12:
    print("Password must be under 12 characters.")
    exit(0)
elif password in BAD_PASSWORDS:
    print("Please choose a stronger password.")
    exit(0)

conf_password = input("Re-enter password:")

if password == conf_password:
    print("Password is correct.")
else:
    print("Error, try again.")
