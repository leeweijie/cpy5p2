# Check if input is a number and convert it to an integer
def process_input():
    global number
    try:
        number = int(number)
        return True
    except ValueError:
        return False

# Get user input
number = input("Enter number: ")

if process_input():
    # Check using remainder when number is divided by 2
    if number % 2 == 1:
        print("{0} is odd".format(number))
    else:
        print("{0} is even".format(number))
else:
    print("Invalid input")
