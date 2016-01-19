from q04_determine_leap_year import check_leap


# Check if inputs are numbers and convert them to integers
def process_input():
    global month
    try:
        month = int(month)
        return True
    except ValueError:
        return False

# Map month number to name
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Get user input
month = input("Enter month: ")
year_input = input("Enter year: ")

if process_input():
    if month == 2:
        if check_leap(year_input):
            print("{0} {1} has 29 days".format(month_names[month-1], year_input))
        else:
            print("{0} {1} has 28 days".format(month_names[month-1], year_input))
    elif month in [4, 6, 9, 11]:
        print("{0} {1} has 30 days".format(month_names[month-1], year_input))
    else:
        print("{0} {1} has 31 days".format(month_names[month-1], year_input))
else:
    print("Invalid input")