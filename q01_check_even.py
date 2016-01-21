from verify_input import verify

# Get user input
number = input("Enter number: ")

if verify(number, "int"):
    number = int(number)
    # Check using remainder when number is divided by 2
    if number % 2 == 1:
        print("{0} is odd".format(number))
    else:
        print("{0} is even".format(number))
else:
    print("Invalid input")
