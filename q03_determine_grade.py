# Check if input is a number and convert it to a float
def process_input():
    global score
    try:
        score=float(score)

        # Make sure score is > 0 and < 100
        if 0 <= score <= 100:
            return True
        else:
            return False
    except ValueError:
        return False

# Get user input
score = input("Enter score: ")


if process_input():

    # Check grade
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 55:
        grade = "C"
    elif score >= 50:
        grade = "D"
    elif score >= 45:
        grade = "E"
    elif score >= 35:
        grade = "S"
    else:
        grade = "U"

    # Print grade
    print(grade)

else:
    print("Invalid input")