# Lab 04 - Data Conversion Utility
# An online shopping system receives product price and quantity as text.

print("==================================================")
print("             DATA CONVERSION UTILITY              ")
print("==================================================")

product_name = input("Enter Product Name : ")
price_str = input("Enter Price        : ")
quantity_str = input("Enter Quantity     : ")

# Convert to appropriate types
price = float(price_str)
quantity = int(quantity_str)
total_price = price * quantity
amount_str = str(total_price)

print()
print("--------------------------------------------------")
print("               TYPE CASTING SUMMARY               ")
print("--------------------------------------------------")
print(f"{'Variable':<15} {'Value':<15} {'Python Type'}")
print("-" * 50)
print(f"{'product_name':<15} {product_name:<15} {type(product_name)}")
print(f"{'price':<15} {price:<15} {type(price)}")
print(f"{'quantity':<15} {quantity:<15} {type(quantity)}")
print(f"{'total_price':<15} {total_price:<15} {type(total_price)}")
print(f"{'amount_str':<15} {amount_str:<15} {type(amount_str)}")

print()
print("--------------------------------------------------")
print("                   TAX INVOICE                    ")
print("--------------------------------------------------")
print(f"  Product Name   : {product_name}")
print(f"  Price per Unit : Rs. {price:.2f}")
print(f"  Quantity       : {quantity}")
print("  " + "-" * 40)
print(f"  Invoice Total  : Rs. {total_price}")
print("==================================================")
