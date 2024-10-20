inventory = []


#notes to self

#the "f" is called an f-string which allows you to embed python expressions inside string literals
#without it, you wouldn't be able to see the name of each item when running the code, it would appear
#as "Item {'name'} added, removed, etc.

def add_item():
    name = input("Please input item name: ")
    price = float(input("Please input item price:"))
    quantity = int(input("Please input item quantity: "))
    category = str(input("Please input item category: "))

    item = {
        "name" : name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    inventory.append(item)
    print(f"Item '{name}' added successfully to market inventory")

def update_item():
    name = input("Enter the item name you want to update: ")
    for item in inventory:
        if item["name"] == name:
            item['price'] = float(input("Enter a new item price: "))
            item['quantity'] = int(input("Enter a new item quantity: "))
            item['category'] = input("Enter a new item category: ")
            print("Item '{name}' updated")
            return
    print(f"Item '{name}' not found")



def view_inventory():
    if not inventory:
        print("The market inventory is empty")
    else:
        print("Inventory: ")
        for item in inventory:
            print(f"name: {item['name']}, price: {item['price']}, quantity: {item['quantity']}, category: {item['category']} ")
        print()


def remove_item():
    name = input("Enter the item you would like to remove from the market inventory: ")
    for item in inventory:
        if item['name'] == name:
            inventory.remove(item)
            print(f" {item['name']} removed from market inventory")
            return
    print(f"Item '{name}' not found")

def search_by_category():
    category = input("Enter the category you wish to search by: ")
    items_in_inventory = [item for item in inventory if item['category'].lower() == category.lower()]
    if not items_in_inventory:
        print("No items found within category '{category}' ")
    else:
        print(f"items in category '{category}': ")
        for item in items_in_inventory:
            print(f"name: {item['name']}, price: {item['price']}, quantity: {item['quantity']}, category: {item['category']} ")
        print()

#This is how you create a "main menu" within a program, utlizing a function
def main_menu():
    while True:
        print("Choose an option: ")
        print("1. Add an Item")
        print("2. Update an Item")
        print("3. View Market Inventory")
        print("4. Remove an Item")
        print("5. Search by Category")

        option = input("Enter your choice by inputting the associated number: ")
#Doing this connects the functions you've created earlier, to the main menu 
        if option == '1':
            add_item()
        elif option == '2':
            update_item()
        elif option == '3':
            view_inventory()
        elif option == '4':
            remove_item()
        elif option == '5':
            search_by_category()
        else:
            print("Invalid input, please try again.")


#This is the function to run a program within python such as this
if __name__ == "__main__":
    main_menu()
