
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password = input("Input password:")
    if len(password) < 8:
        print("Password must be over 8 characters.")
        continue
    elif len(password) > 12:
        print("Password must be under 12 characters.")
        continue
    elif password in BAD_PASSWORDS:
        print("Please choose a stronger password.")
        continue
    conf_password = input("Re-enter password:")

    if password == conf_password:
        print("Password is correct.")
        continue
    else:
        print("Error, try again.")
        break
exit(0)
