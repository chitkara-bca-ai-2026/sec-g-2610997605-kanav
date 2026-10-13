# Lab 03 - Student Record Display
# A school needs to collect and display basic details of a student.

print("========================================")
print("          STUDENT RECORD DISPLAY        ")
print("========================================")

# 1. Take input from user
name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

# 2. Display details in formatted output
print()
print("----------------------------------------")
print("Student Details:")
print(f"   Name  : {name}")
print(f"   Age   : {age}")
print(f"   Marks : {marks}")
print("----------------------------------------")
