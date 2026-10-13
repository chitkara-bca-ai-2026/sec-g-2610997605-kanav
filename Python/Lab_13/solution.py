# Lab 13 - Inventory Control System
# Interactive, menu-driven Python program managing inventory

inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("==================================================")
print("             INVENTORY CONTROL SYSTEM             ")
print("==================================================")

while True:
    print()
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        print()
        print("--- Current Inventory ---")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")
            
    elif choice == "2":
        item_to_add = input("Enter item name to add: ").strip()
        inventory.append(item_to_add)
        print(f"[SUCCESS] \"{item_to_add}\" added to inventory.")
        
    elif choice == "3":
        item_to_remove = input("Enter item name to remove: ").strip()
        if item_to_remove in inventory:
            inventory.remove(item_to_remove)
            print(f"[SUCCESS] \"{item_to_remove}\" removed from inventory.")
        else:
            print(f"[ERROR] \"{item_to_remove}\" not found in inventory.")
            
    elif choice == "4":
        inventory.sort()
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")
            
    elif choice == "5":
        print("Thank you for using the Inventory Control System. Goodbye!")
        break
        
    else:
        print("[ERROR] Invalid choice! Please select a valid option from 1 to 5.")
