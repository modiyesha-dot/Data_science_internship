#Student Performance Analyzer

#Variables and Data Types

student_name = "Yesha Modi"
python_marks = 92
sql_marks = 88
power_bi_marks = 80
attendance = 89.5

#Total and Average (Operators)

total_marks = python_marks + sql_marks + power_bi_marks
average_marks = total_marks/3

#Function to calculate grade

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

#Function to check attendance

def attendance_status(att):
    if att >= 75:
        return "Eligible for exam"
    return "Not eligible for exam"

#Output

print("\n------- STUDENT REPORT -------")
print(f"Student Name : {student_name}")
print(f"Total Marks : {total_marks}")
print(f"Average Marks : {average_marks:.2f}")
print(f"Grade : {calculate_grade(average_marks)}")
print(f"Attendance : {attendance}%")
print(f"Status : {attendance_status(attendance)}")

#Loop

print("\nSubject Marks:")
subjects = {"Python" : python_marks , "SQL" : sql_marks , "Power BI" : power_bi_marks}
for subjects , marks in subjects.items():
    print(f"{subjects} : {marks}")
print("\nProgram executed successfully!")