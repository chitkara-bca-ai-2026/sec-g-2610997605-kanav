# Lab 14 - Library Book Collection
# Catalog book records using tuples and sets

books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = {category for _, _, _, category in books}
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("==================================================")
print("          LIBRARY BOOK & CATEGORY MANAGER         ")
print("==================================================")

while True:
    print()
    print("Select an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ").strip()
    
    if choice == "1":
        print()
        print("--- Current Library Catalog (Fixed Records) ---")
        for i, book in enumerate(books, 1):
            title, author, year, category = book
            print(f"{i}. \"{title}\" by {author} ({year}) | Genre: {category}")
        print(f"Total Books: {len(books)}")
        
    elif choice == "2":
        print()
        print("--- Add New Book Record ---")
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year = input("Enter publication year: ").strip()
        category = input("Enter category/genre: ").strip()
        
        if title and author and year and category:
            new_book = (title, author, year, category)
            books.append(new_book)
            library_categories.add(category)
            print(f"[SUCCESS] \"{title}\" added as an immutable catalog record.")
            print(f"[INFO] Category set updated with: \"{category}\"")
        else:
            print("[ERROR] All fields are required.")
            
    elif choice == "3":
        print()
        print("--- Unique Categories Available in Library (Set) ---")
        for cat in sorted(library_categories):
            print(f" - {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")
        
    elif choice == "4":
        print()
        print("--- Add to Student Wishlist ---")
        req_genre = input("Enter requested category: ").strip()
        if req_genre:
            student_wishlist.add(req_genre)
            print(f"[SUCCESS] \"{req_genre}\" added to student wishlist.")
            
    elif choice == "5":
        print()
        print("==================== CATEGORY GAP ANALYSIS ====================")
        print(f"Library Holdings (Set): {sorted(list(library_categories))}")
        print(f"Student Wishlist (Set): {sorted(list(student_wishlist))}")
        print("----------------------------------------------------------------")
        in_stock = library_categories & student_wishlist
        purchase_order = student_wishlist - library_categories
        combined = library_categories | student_wishlist
        
        print(f"1. Already in Stock (Intersection &):\n   {sorted(list(in_stock))}\n")
        print(f"2. Purchase Order Needed (Difference -):\n   {sorted(list(purchase_order))}\n")
        print(f"3. Full Combined Genre Coverage (Union |):\n   {sorted(list(combined))}")
        print("================================================================")
        
    elif choice == "6":
        print()
        print("Thank you for using the Library Manager. Goodbye!")
        break
        
    else:
        print("[ERROR] Invalid choice! Please select an option between 1 and 6.")
