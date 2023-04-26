# ----------------------------------------------------------------
# Author:
# Date:
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    # Check if the student is in-state
    in_state = s_in_state.get(id, False)

    # Get the list of courses the student is registered for
    courses = []
    for course, roster in c_rosters.items():
        if id in roster:
            courses.append(course)

    # Calculate the total number of course hours
    total_hours = sum([c_hours.get(course, 0) for course in courses])

    # Calculate the tuition cost
    if in_state:
        tuition_rate = 150
    else:
        tuition_rate = 450

    tuition_cost = total_hours * tuition_rate

    return total_hours, tuition_cost
    # ------------------------------------------------------------
    # This function calculate billing information. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # This function returns the number of course hours and tuition
    # cost.
    # ------------------------------------------------------------
    #pass  # temporarily avoid empty function definition


def display_hours_and_bill(hours, cost):
    print("Total course hours:", hours)
    print("Total tuition cost:", cost)
    # ------------------------------------------------------------
    # This function prints the number of course hours the student
    # is taking and the total tuition cost. It takes two parameters:
    # hours and cost. This function has no return value.
    # ------------------------------------------------------------
    #pass  # temporarily avoid empty function definition
