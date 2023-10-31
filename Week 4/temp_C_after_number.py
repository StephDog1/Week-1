def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    input_str = input("Enter a temperature in Centigrade: ")

    if input_str.endswith('C'):
        try:
            celsius = float(input_str[:-1])
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}C is equal to {fahrenheit:.2f}F")
        except ValueError:
            print("Invalid input format. Please provide a numeric temperature followed by 'C'.")
    else:
        print("Invalid input format. Please provide a temperature followed by 'C'.")

if __name__ == "__main__":
    main()
