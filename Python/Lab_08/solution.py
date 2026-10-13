# Lab 08 - School Result Processing
# Student Grade Evaluation System

print("==================================================")
print("             SCHOOL RESULT PROCESSING             ")
print("==================================================")

name = input("Enter Student Name : ")
roll_no = input("Enter Roll Number  : ")

marks = []
has_failed = False

print()
print("--- Enter Marks for 5 Subjects (0-100) ---")
for i in range(1, 6):
    m = float(input(f"Enter marks for Subject {i}: "))
    if m < 0 or m > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()
    if m < 40:
        has_failed = True
    marks.append(m)

total_marks = sum(marks)
percentage = (total_marks / 500.0) * 100.0

if has_failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remark = "Pass"
    else:
        result = "FAIL"
        grade = "F"
        remark = "Fail"

print()
print("==================================================")
print("               STUDENT REPORT CARD                ")
print("==================================================")
print(f"  Student Name : {name}")
print(f"  Roll Number  : {roll_no}")
print("  " + "-" * 46)
print(f"  Total Marks  : {total_marks} / 500.0")
print(f"  Percentage   : {percentage:.2f}%")
print(f"  Result       : {result}")
print(f"  Grade        : {grade}")
print(f"  Remarks      : {remark}")
print("==================================================")
