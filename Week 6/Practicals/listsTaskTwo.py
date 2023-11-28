all_users = ["Hello", "Goodbye", "1111111111111", "ThisIsABadPassword", "1234567"]

some_users = [u for u in all_users if len(u) < 8]
print(some_users)