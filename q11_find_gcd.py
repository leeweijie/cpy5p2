from verify_input import verify

# Get user input
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

if verify([first_number, second_number], "int") and int(first_number) != 0 and int(second_number) != 0:
    first_number, second_number = int(first_number), int(second_number)
    # Let d be the divisor / multiple
    # Set d to the smaller of the 2 numbers
    d = min(first_number, second_number)

    while first_number % d != 0 or second_number % d != 0:
        d -= 1

    # Print the greatest common divisor
    print(d)
else:
    print("Invalid input")
