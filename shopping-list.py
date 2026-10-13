# Start with an empty list
shopping_list = []

while True:
    print("\n--- Shopping List Menu ---")
    print("Options: add / remove / show / done")
    choice = input("Enter your choice: ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' has been added to your list.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        # Check membership with 'in' before calling .remove() to prevent crashing
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        print("\nCurrent Shopping List:")
        if not shopping_list:
            print("Your list is empty.")
        else:
            for item in shopping_list:
                print(f"- {item}")

    elif choice == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid choice. Please choose from add, remove, show, or done.")
