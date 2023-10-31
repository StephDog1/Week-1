def single_int_parameter(sin_int):
    """Accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive),
    or False otherwise."""
    return 0 <= sin_int <= 100


int1 = int(input("Enter a single integer:"))

result = single_int_parameter(int1)
print(result)
