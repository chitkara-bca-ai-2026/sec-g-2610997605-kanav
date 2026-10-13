# Lab 07 - Calendar Verification System
# A calendar application needs to determine whether a given year is a leap year.

print("==================================================")
print("             CALENDAR VERIFICATION SYSTEM         ")
print("==================================================")

year = int(input("Enter year: "))

# Validation: ensure positive integer greater than 0
if year <= 0:
    print("Error: Year must be a positive integer greater than 0.")
    exit()

# Check leap year rules using if-else
if year % 100 == 0:
    if year % 400 == 0:
        is_leap = True
        reason = "Century year divisible by 400"
    else:
        is_leap = False
        reason = "Century year not divisible by 400"
elif year % 4 == 0:
    is_leap = True
    reason = "Divisible by 4 and not a century year"
else:
    is_leap = False
    reason = "Not divisible by 4"

if is_leap:
    status = "LEAP YEAR"
    days_in_year = 366
    days_in_feb = 29
else:
    status = "COMMON YEAR"
    days_in_year = 365
    days_in_feb = 28

print()
print("--------------------------------------------------")
print(f"Year: {year}")
print(f"Status: {status}")
print(f"Days in Year: {days_in_year} days")
print(f"Days in February: {days_in_feb} days")
print(f"Reason: {reason}")
print("--------------------------------------------------")
