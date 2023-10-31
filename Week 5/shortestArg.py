import sys


def main():
    arguments = sys.argv[1:]

    if not arguments:
        print("No arguments provided.")
    else:
        shortest_arg = min(arguments, key=len)
        print(f"The smallest argument is: {shortest_arg}")


if __name__ == "__main__":
    main()
