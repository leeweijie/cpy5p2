from verify_input import verify

# Get user input
number = input("Enter number: ")

# Initialise factors variable
factors = []
if verify(number, "int") and int(number) > 0:
    number = int(number)
    # Special case as the range in the for loop below starts from 2
    if number == 1:
        factors = [1]
    elif number >= 2:
        for i in range(2, number + 1):
            while number % i == 0:
                number /= i
                factors.append(i)

    print(*factors, sep=', ')
