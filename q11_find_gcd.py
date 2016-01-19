# Check if input are numbers and convert them to integers
def process_input():
    global first_number, second_number
    try:
        first_number = int(first_number)
        second_number = int(second_number)
        if first_number == 0 or second_number == 0:
            return False
        return True
    except ValueError:
        return False

# Get user input
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

if process_input():
    # Let d be the divisor / multiple
    # Set d to the smaller of the 2 numbers
    d = min(first_number, second_number)

    while first_number % d != 0 or second_number % d != 0:
        d -= 1

    # Print the greatest common divisor
    print(d)
else:
    print("Invalid input")