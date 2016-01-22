from verify_input import verify

# Get user input
number_of_students = input("Enter the number of students: ")
if verify(number_of_students, "int") and int(number_of_students) >= 2:
    # Convert string input to int
    number_of_students = int(number_of_students)
    # Store the strings for recursive input
    prompt1 = "Enter name of student {0}: "
    prompt2 = "Enter score of student {0}: "
    try:
        students = [(input(prompt1.format(i + 1)), float(input(prompt2.format(i + 1)))) for i in
                    range(number_of_students)]
        # Sort the list by the second object of the tuples
        students = sorted(students, key=lambda x: x[1], reverse=True)
        # Print result
        print("Highest scorer is {0} with a score of {1}".format((students[0])[0], (students[0])[1]))
        print("Second highest scorer is {0} with a score of {1}".format((students[1])[0], (students[1])[1]))
    except ValueError:
        print("Invalid input")
else:
    print("Invalid input")
