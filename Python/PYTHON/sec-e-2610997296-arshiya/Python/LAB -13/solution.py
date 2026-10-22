#Initialize Inventory
inventory = ["Notebook", "Pen", "Eraser", "Ruler", "Marker"]

#Function to display the inventory
def display_inventory():
    print("Current Inventory:")
    for item in inventory:# for i in range (len(inventory)):   #print(f"{i+1}.{inventory[i]}")
        print(f"- {item}")
#1.View 2. Add 3. Remove 4. Sort 5. Exit
#Prompt: Input Choice(1-5):
while True:
    choice = int(input("Enter your choice (1-5): "))

    #choice 1
    if choice == 1:
        display_inventory()

    #choice 2 
    # we can use title and particular space to add the item in the inventory , it will look more organized and readable.
    elif choice == 2:
        new_item = input("Enter the item to add: ")
        inventory.append(new_item)
        print(f"{new_item} has been added to the inventory.")
        display_inventory()

    #choice 3
    elif choice == 3:
        remove_item = input("Enter the item to remove: ")
        if remove_item in inventory:
            inventory.remove(remove_item)
            print(f"{remove_item} has been removed from the inventory.")
        else:
            print(f"{remove_item} is not in the inventory.")

    #choice 4
    elif choice == 4:
        inventory.sort()
        print("Inventory has been sorted.")
        display_inventory()

    #Choice 5 (exit the loop)
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

    


