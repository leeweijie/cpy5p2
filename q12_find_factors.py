from verify_input import verify

# Get user input
number = input("Enter number: ")

# Initialise factors variable
factors = []
if verify(number, "int") and int(number) > 0:
    # Convert string input to int
    number = int(number)
    # Special case as the range in the for loop starts from 2
    if number == 1:
        factors = [1]
    else:
        for i in range(2, number + 1):
            while number % i == 0:
                number /= i
                factors.append(i)
    # Print array without square brackets
    print(*factors, sep=', ')
else:
    print("Invalid input")
