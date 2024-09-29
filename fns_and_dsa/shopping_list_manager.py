def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")  # Prompt the user to choose an option

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the name of the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the name of the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        
        elif choice == '3':
            # Display the current shopping list
            if shopping_list:
                print("\nYour current shopping list:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
