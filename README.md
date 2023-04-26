# GroupProject

CSC121	PYTHON Programming	
_______________________________________________________________________


Group Project
Objectives

In this project, students will learn:
- How to work within a team to create a Python program
- How to create modules and functions
- How to pass data from one function to another
- How to store data in lists and dictionaries
- How to create and use selection control structures
- How to create and use iterative control structures
- How to add comments to Python code
Goals

In this project, students will demonstrate the abilities to:
- Work in teams to create Python programs
- Create modules and functions
- Pass data from one function to another
- Store data in lists and dictionaries
- Create and use selection control structures
- Create and use iterative control structures
- Add comments to Python code
Project Description

You have learned quite a lot about the basics of Python programming.  In this project, you will integrate what you have learned to develop a larger program.

This program creates a class registration system.  Students log into the class registration system and then they can add courses, drop courses, and list the courses for which they have registered.

This program has 7 functions in 3 modules: a student module, a billing module, and a main module.

Module: student.py
You must define the following functions in the student module.


Module: billing.py
You must define the following functions in the billing module.



Module: registration.py (main module)
You must define the following functions in the main module.




This program uses lists and dictionaries to store data. To make grading easier, data will be added to these variables at the beginning of the main function.

student_list = [('1001', '111'), ('1002', '222'),
				('1003', '333'), ('1004', '444')]
student_in_state = {'1001': True,
			 '1002': False,
			 '1003': True,
			 '1004': False}

course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
course_roster = {'CSC101': ['1004', '1003'],
		    'CSC102': ['1001'],
		    'CSC103': ['1002'],
		    'CSC104': []}
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

There are 4 students in this program.  ID and PIN of students are stored as tuples in student_list.  The first element of each tuple is student ID and the second element is the PIN.

Students that are in-state are stored in the student_in_state dictionary. Students 1001 and 1003 are in-state students.

Four courses are offered. Each course has a number of credit hours. The courses and credit hour information are stored in course_hours: 
CSC101 has 3 credit hours. 
CSC102 has 4 credit hours. 
CSC103 has 5 credit hours. 
CSC104 has 3 credit hours.

The maximum class size of the courses offered are stored in course_max_size.  The max sizes of CSC101, CSC102, CSC103, and CSC104 are 3, 2, 1, and 3 respectively.

Rosters of the four classes offered are stored as four lists which are values of the course_roster dictionary:  
Students 1004 and 1003 are enrolled in CSC101.  
Student 1001 is enrolled in CSC102.  
Student 1002 is enrolled in CSC103. 
No one is enrolled in CSC104.

The data given above must be used in the program as specified above. Any changes to how the data is structured must be proposed as a specification change to the instructor and approved by the instructor.

The program should have a loop to create multiple student sessions.  In each session, ask the user to enter an ID, then call the login function to verify the student’s identity.  If login is successful, use a loop to allow the student to add courses, drop courses, list courses registered, or display a bill.

The following is an example.

Enter ID to log in, or 0 to quit: 1234
Enter PIN: 123
ID or PIN incorrect

Enter ID to log in, or 0 to quit: 1001
Enter PIN: 111
ID and PIN verified

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC121
Course not found

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC102
You are already enrolled in that course.

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC103
Course already full.

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC101
Course added

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 4
Course load: 7 credit hours
Enrollment cost: $1575.00

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 2
Enter course you want to drop: CSC121
Course not found

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 2
Enter course you want to drop: CSC103
You are not enrolled in that course.

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 2
Enter course you want to drop: CSC102
Course dropped

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 3
Courses registered:
CSC101
Total number: 1

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC102
Course added

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 3
Courses registered:
CSC101
CSC102
Total number: 2

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 4
Course load: 7 credit hours
Enrollment cost: $1575.00

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 0
Session ended.

Enter ID to log in, or 0 to quit: 1002
Enter PIN: 222
ID and PIN verified

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 3
Courses registered:
CSC103
Total number: 1

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC101
Course already full.

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC102
Course added

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 3
Courses registered:
CSC102
CSC103
Total number: 2

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 4
Course load: 9 credit hours
Enrollment cost: $7650.00

Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: 0
Session ended.

Enter ID to log in, or 0 to quit: 0

Programs will be graded based on both functionality and code readability. A working program could still have points deducted for sloppy or difficult to understand code. All code should have module and function comment headers plus appropriate in-line comments.

As with all assignments, the Academic Integrity Policy is in effect, and cheating (including copying published solutions from the Internet) will result in a 0 for the entire team.
Program Submission Requirements

You must create three Python files: 
The student module named student.py
The billing module named billing.py
The main module named registration.py

One member of your programming team should submit the three Python files to Blackboard in a zip file called GroupProject.zip. Other team members do not need to submit any files to Blackboard. 

All team members should type the names of all the group members that worked on the project in the Text Submission area of the assignment. 
Deviations from Project Specification

This document should be treated as a formal project specification, and as such, you should follow all directions and produce output as specified in the example output above. Any unapproved deviation from these instructions will result in reductions in credit.

Some deviation or creativity MAY be considered with the following guidelines:
Any program differences from this specification should be proposed to the instructor via email at least 1 week before the project submission deadline for approval. 
The change proposal should be at least 3 sentences that describe the desired change, the reason for changing, and the expected learning outcome.
The instructor reserves the right to NOT approve specification change requests, however a decision will be rendered within 48 hours of the request. As the primary stakeholder, the decision of the instructor is final.
Proposed and approved changes to the program that are subsequently implemented may enable students to receive up to 25 additional extra credit points to be added to the project grade.
Any extra credit awarded will be based on the amount of additional work beyond the original assignment, the utility of the improvements to the course registration system, and the level of innovation or creativity in the changes.
Extra credit is only eligible to working programs that still cover the functionality of the original specification.
Presentation Format

Each team will give a 5 to 10-minute presentation. You need to do the following in the presentation:

Describe how the work was distributed (e.g. who did what?)
Demonstrate your program to show that it works

Additionally, you can answer the following during your presentation or answer them afterwards as follow-up questions:

Did you encounter any difficulties? If so, how did you overcame them?
What you have learned from this experience?

In addition to the presentation, the instructor may ask follow-up questions on your project and presentation.

The presentation may be formal or informal, with or without PowerPoint slides. Teams should be prepared to screenshare to demonstrate their project and show their code. Presentations must not go over 10 minutes, and the instructor will monitor the time.

Any or all students on the team may give the group presentation, but ALL team members must be present during the team’s presentation time, and each must be prepared to answer questions. Audio, video, and internet connections should be checked before the presentation to ensure participation. Lack of audio, video, or internet connection is not an allowed excuse to meet or not participate in this group presentation. All students will be graded based on team AND individual performance.

The instructor will provide a choice of days and times your team can choose from to do your presentation via Teams. This presentation will be done after submitting your project.

You should consider this presentation as though it were a business meeting in a software company. Ensure you are wearing appropriate attire and are presenting from a suitable location.
Grading Rubric

Functional project working to specification (Application Development) [50 points]
All test cases pass with no issue. Test cases include the example output above with additional ad hoc testing.

Project code with appropriate comments and formatting (Quality and Secure Code) [10 points]
Module and function header comments and other appropriate comments
Well-formatted code with few PEP 8 violations

Project presentation (Effective Communication) [20 points]
Well organized and informative presentation given in the time limit
Present with video and audio
Appropriate attire in appropriate setting
Responsive to questions with thoughtful answers

Peer evaluation (Teamwork) [20 points]
Submission of peer evaluation
NOTE: If peer evaluation is not submitted, all points are forfeited for this category.
Thoughtfulness and insights provided in evaluation
Input from peers on teammate’s contribution and performance

Extra credit for approved and implemented changes [25 points]
Innovation and creativity of proposal
Amount of participation on team in designing and implementing extra credit
Amount of work involved in completing extra credit features
