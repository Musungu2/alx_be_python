def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added to your shopping list.")

        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from your shopping list.")
            else:
                print(f"{item} is not in your shopping list.")

        elif choice == 3:
            print("\nYour Shopping List:")
            if not shopping_list:
                print("Your list is empty.")
            else:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
