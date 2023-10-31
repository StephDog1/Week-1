max_temp = float("-inf")
min_temp = float("inf")
temp_sum = 0.0
count = 0

while True:
    try:
        user_input = input("Enter a temperature (or press Enter to finish): ")
        if not user_input:
            break

        temperature = float(user_input)
        temp_sum += temperature
        count += 1
        if temperature > max_temp:
            max_temp = temperature
        if temperature < min_temp:
            min_temp = temperature
    except ValueError:
        print("Invalid input. Please enter a valid temperature.")

if count == 0:
    print("No valid temperatures were entered.")
else:
    mean_temp = temp_sum / count

    print(f"Maximum temperature: {max_temp}")
    print(f"Minimum temperature: {min_temp}")
    print(f"Mean temperature: {mean_temp:.2f}")
