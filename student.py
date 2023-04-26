# ----------------------------------------------------------------
# Author:
# Date:
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

def list_courses(id, c_roster):
    count = 0  # initialize course count to 0

    # loop through each course in the class roster
    for course in c_roster:

        # check if the student is enrolled in the course
        if id in course:
            # if the student is enrolled, display the course
            print(course[0])

            # increment the course count
            count += 1

    # display the total number of courses
    print("Total number of courses: ", count)

    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has two parameters: id is the ID of the
    # student; c_roster is the list of class rosters. This function
    # has no return value.
    # -------------------------------------------------------------
    #pass  # temporarily avoid empty function definition


def add_course(id, c_roster, c_max_size):
    # ask user to enter the course they want to add
    course = input("Enter the course you want to add: ")

    # check if the course exists
    if course not in [c[0] for c in c_roster]:
        print("Error: course not offered")
        return

    # loop through each course in the class roster
    for c in c_roster:

        # check if the course is the one the student wants to add
        if c[0] == course:

            # check if the student is already enrolled in the course
            if id in c:
                print("Error: student already enrolled in this course")
                return

            # check if the course is full
            if len(c) == c_max_size[c_roster.index(c)] + 1:
                print("Error: course is full")
                return

            # if everything is okay, add student ID to the course's roster
            c.append(id)
            print("Student added to", course, "roster")

    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
   # pass  # temporarily avoid empty function definition


def drop_course(id, c_roster):
    def drop_course(id, c_roster):
        # Ask user to enter the course to be dropped
        course_to_drop = input("Enter the course to drop: ")

        # Find the course in the roster
        course_found = False
        for i in range(len(c_roster)):
            if c_roster[i][0] == course_to_drop:
                course_found = True
                course_index = i
                break

        # If the course is not found, display error message and stop
        if not course_found:
            print("Error: Course not found")
            return

        # Check if the student is enrolled in the course
        student_found = False
        for student in c_roster[course_index][1]:
            if student == id:
                student_found = True
                break

        # If the student is not enrolled in the course, display error message and stop
        if not student_found:
            print("Error: Student is not enrolled in the course")
            return

        # Remove the student ID from the course roster
        c_roster[course_index][1].remove(id)

        # Display success message
        print(f"Student {id} has been dropped from course {course_to_drop}")

    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------
    #pass  # temporarily avoid empty function definition
