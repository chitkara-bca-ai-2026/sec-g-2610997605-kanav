# Lab 06 - Shop Billing System
# Develop a Python program for a Clothing Store Billing System.

print("==================================================")
print("           CLOTHING STORE BILLING SYSTEM          ")
print("==================================================")

cust_name = input("Enter Customer Name: ")
garment_name = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
qty = int(input("Enter Number of Garments: "))

total_cost = price * qty

print()
print("==================================================")
print("                       BILL                       ")
print("==================================================")
print(f"  Customer Name : {cust_name}")
print(f"  Garment Name  : {garment_name}")
print(f"  Price per Unit: Rs. {price}")
print(f"  Quantity      : {qty}")
print(f"  Total Amount  : Rs. {total_cost}")
print("==================================================")
