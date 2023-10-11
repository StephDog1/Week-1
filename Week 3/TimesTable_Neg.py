nr = int(input("Please enter a number:"))

if nr < 0:
    for n in range(-12, 0):
        print(nr, "x", n, "=", nr * n)
for n in range(1, 13):
    print(nr, "x", n, "=", nr * n)
