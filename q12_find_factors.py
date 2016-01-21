# Check if input is a number and convert it to an integer
def process_input():
    global number
    try:
        number = int(number)
        if number <= 0:
            return False
        return True
    except ValueError:
        return False

# Get user input
number = input("Enter number: ")

# Initialise factors variable
factors = []
if process_input():

    # Special case as the range in the for loop below starts from 2
    if number == 1:
        factors = [1]
    elif number >= 2:
        for i in range(2, number + 1):
            while number % i == 0:
                number /= i
                factors.append(i)

    print(*factors, sep=', ')
