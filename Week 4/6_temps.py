max_temp = float("-inf")
min_temp = float("inf")
temp_sum = 0.0

for i in range(1, 7):
    try:
        temperature = float(input(f"Enter temperature {i}: "))
        temp_sum += temperature
        if temperature > max_temp:
            max_temp = temperature
        if temperature < min_temp:
            min_temp = temperature
    except ValueError:
        print("Invalid input. Please enter a valid temperature.")

mean_temp = temp_sum / 6

# Display the results
print(f"Maximum temperature: {max_temp}")
print(f"Minimum temperature: {min_temp}")
print(f"Mean temperature: {mean_temp:.2f}")
