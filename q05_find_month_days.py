from verify_input import verify

# Import function from leap years module
from q04_determine_leap_year import check_leap

# Map month number to name
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]

# Get user input
month = input("Enter month: ")
year = input("Enter year: ")

if verify([month, year], "int"):
    month, year = int(month), int(year)
    if month == 2:
        # Number of days in February is dependent on whether it is a leap year
        if check_leap(year):
            print("{0} {1} has 29 days".format(month_names[month - 1], year))
        else:
            print("{0} {1} has 28 days".format(month_names[month - 1], year))
    elif month in [4, 6, 9, 11]:
        print("{0} {1} has 30 days".format(month_names[month - 1], year))
    else:
        print("{0} {1} has 31 days".format(month_names[month - 1], year))
else:
    print("Invalid input")
