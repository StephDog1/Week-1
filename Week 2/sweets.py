nr_sweets = int(input("How many sweets are there?:"))
nr_pupils = int(input("How many pupils are there?:"))
sweets_pupils = int(nr_sweets / nr_pupils)
left_over = nr_sweets -(nr_pupils * sweets_pupils)

print(f"Give {sweets_pupils} sweets to each pupil. There will be {left_over} sweets left over.")
