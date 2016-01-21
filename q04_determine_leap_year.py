def check_leap(year):
    year = int(year)

    # Return True if it is a leap year, False if it is not
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


# Code below is only executed if module is ran as a standalone program, not as an imported module
if __name__ == "__main__":
    # Get user input
    year_input = input("Enter year: ")
    if check_leap(year_input):
        print("Leap")
    else:
        print("Non-leap")
