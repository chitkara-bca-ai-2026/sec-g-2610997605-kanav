# Lab 02 - Employee Information System
# A company needs to store employee details.

# Take input from the user
emp_name = input("Enter Employee Name: ")
print(f"  Data type: {type(emp_name)}")

emp_id = int(input("Enter Employee ID: "))
print(f"  Data type: {type(emp_id)}")

salary = float(input("Enter Salary: "))
print(f"  Data type: {type(salary)}")

department = input("Enter Department: ")
print(f"  Data type: {type(department)}")

active_input = input("Is the employee active? (yes/no): ")
is_active = active_input.lower() == "yes"
print(f"  Data type: {type(is_active)}")

# Display employee details
print()
print("--- Employee Details ---")
print(f"Name       : {emp_name}")
print(f"ID         : {emp_id}")
print(f"Salary     : {salary}")
print(f"Department : {department}")
print(f"Active     : {is_active}")
