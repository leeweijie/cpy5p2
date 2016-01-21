from verify_input import verify

# Get user input
score = input("Enter score: ")

if verify(score, "float") and 0 <= (float(score)) <= 100:
    # Convert string input to float
    score = float(score)
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
