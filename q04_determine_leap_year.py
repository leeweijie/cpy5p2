# Check if input is a number and convert it to an integer
def verify_input(user_input):
    try:
        user_input = int(user_input)
        return True
    except ValueError:
        return False


def check_leap(year):
    if verify_input(year):
        year = int(year)

        # Return True if it is a leap year, False if it is not
        if year % 4 != 0:
            return False
        # A little repetition here, but variables are not used to store the quotient for next test to simplify code
        elif year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        print("Invalid input")

# Code below is only executed if module is ran as a standalone program, not as an imported module
if __name__=="__main__":
    # Get user input
    year_input = input("Enter year: ")
    if check_leap(year_input):
        print("Leap")
    else:
        print("Non-leap")
