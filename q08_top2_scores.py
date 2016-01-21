from verify_input import verify


def score_compare():
    # Get user input
    number_of_students = input("Enter the number of students: ")
    if verify(number_of_students, "int") and int(number_of_students) >= 2:
        # Convert string input to int
        number_of_students = int(number_of_students)

        # Initialise array
        students = []

        for i in range(number_of_students):
            student_name = input("Enter name of student {0}: ".format(i + 1))
            student_score = input("Enter score of student {0}: ".format(i + 1))
            if verify(student_score, "float"):
                # Convert string input to float
                student_score = float(student_score)
            else:
                print("Invalid input")
                return
            # Add tuple containing a pair of name and score to array
            students.append((student_name, student_score))

        # Sort the list by the second object of the tuples
        students = sorted(students, key=lambda x: x[1], reverse=True)
        # Print result
        print("Highest scorer is {0} with a score of {1}".format((students[0])[0], (students[0])[1]))
        print("Second highest scorer is {0} with a score of {1}".format((students[1])[0], (students[1])[1]))
    else:
        print("Invalid input")

score_compare()
