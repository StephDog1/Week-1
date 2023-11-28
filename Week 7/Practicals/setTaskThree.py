names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}


name = input("Enter your name: ")
if name not in names:
    print("You are not listed in the set of known names")
else:
    print("You are listed in the set of known names")