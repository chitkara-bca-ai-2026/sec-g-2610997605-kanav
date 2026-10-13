# Lab 05 - Engineering Calculation Tool
import math

print("==================================================")
print("           ENGINEERING CALCULATION TOOL           ")
print("==================================================")

val = float(input("Enter a numerical value: "))
exp = float(input("Enter an exponent: "))
dec_val = float(input("Enter a decimal measurement: "))

power_res = math.pow(val, exp)
sqrt_res = math.sqrt(val)
ceil_res = math.ceil(dec_val)
floor_res = math.floor(dec_val)

print()
print("--- Results ---")
print(f"  Value             : {val}")
print(f"  Exponent          : {exp}")
print(f"  Power (pow)       : {power_res}")
print(f"  Square Root (sqrt): {sqrt_res:.4f}")
print(f"  Decimal Value     : {dec_val}")
print(f"  Ceil Value        : {ceil_res}")
print(f"  Floor Value       : {floor_res}")
print("==================================================")
