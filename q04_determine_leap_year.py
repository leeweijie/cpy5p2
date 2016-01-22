from verify_input import verify


def check_leap(year):
    # Return True if it is a leap year, False if it is not
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


# Code below is only executed if module is ran as a standalone program, not as an imported module
if __name__ == "__main__":
    # Get user input
    year_input = input("Enter year: ")
    if verify(year_input, "int"):
        # Convert string input to int
        year_input = int(year_input)
        # Check and print result
        if check_leap(year_input):
            print("Leap")
        else:
            print("Non-leap")
    else:
        print("Invalid input")
