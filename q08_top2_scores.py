# Check if input is a number and convert it to an integer
number_of_students = 0


def process_input():
    try:
        global number_of_students
        number_of_students = int(number_of_students)
        if number_of_students < 2:
            return False
        return True
    except ValueError:
        return False

def score_compare():
    global number_of_students
    # Get user input
    number_of_students = input("Enter the number of students: ")
    if process_input():

        # Initialise array
        students = []

        for i in range(number_of_students):
            student_name = input("Enter name of student {0}: ".format(i+1))
            student_score = input("Enter score of student {0}: ".format(i+1))
            try:
                student_score = float(student_score)
            except ValueError:
                print("Invalid input")
                return
            # Add tuple containing a pair of name and score to array
            students.append((student_name, student_score))

        # Sort the list by the second object of the tuples
        sorted(students, key=lambda x: x[1])
        # Print result
        print("Highest scorer is {0} with a score of {1}".format((students[0])[0], (students[0])[1]))
        print("Second highest scorer is {0} with a score of {1}".format((students[1])[0], (students[1])[1]))
    else:
        print("Invalid input")

score_compare()
