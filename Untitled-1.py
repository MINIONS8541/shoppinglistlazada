try:
    with open("input.txt", "x") as f:
        f.write("Hello, World!")
except FileExistsError:
    print("File already exists")
else:
    print("File created successfully")




while True:
    print("\nShopping List Menu")
    print("1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(item, "added to the list.")

    elif choice == "2":
        print("\nShopping List:")
        if len(shopping_list) == 0:
            print("The list is empty.")
        else:
            for item in shopping_list:
                print("-", item)
