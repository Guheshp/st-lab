
#---------------------- term work 8 ---- absolute letter grading procedure
per = float(input("Enter the percentage: "))

if per < 0 or per > 100:
    print("Enter valid percentage")
else:
    if per >= 90:
        grade = 'A'
    elif per >= 80:
        grade = 'B'
    elif per >= 70:
        grade = 'C'
    elif per >= 60:
        grade = 'D'
    else:
        grade = 'E'

    grade_messages = {
        'A': "EXCELLENT",
        'B': "Very Good",
        'C': "Good",
        'D': "Above Average",
        'E': "fail"
    }

    print(grade_messages.get(grade, "Invalid grade"), f"\t The percentage = {per} and grade is {grade}")