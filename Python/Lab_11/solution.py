# Lab 11 - Online Account Registration
# Validate password based on specified rules

username = input("Enter your username: ")
password = input("Enter your password: ")

# Check rules
rule_length = len(password) >= 8
rule_digit = any(c.isdigit() for c in password)
rule_upper = any(c.isupper() for c in password)

all_pass = rule_length and rule_digit and rule_upper

print("==================================================")
print("PASSWORD VALIDATION REPORT")
print("==================================================")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print()
print("--- Validation Rules ---")
len_status = "PASS" if rule_length else "FAIL"
digit_status = "PASS" if rule_digit else "FAIL"
upper_status = "PASS" if rule_upper else "FAIL"

print(f"[{len_status}] Minimum 8 characters ({len(password)} characters)")
print(f"[{digit_status}] At least one digit")
print(f"[{upper_status}] At least one uppercase letter")
print()
print("--- Result ---")
if all_pass:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")
print("==================================================")
