shoppingItems = ["Milk", "Bread", "Eggs", "Jam", "Apple", "OOSpam", "Orange", "Butter"]



for item in shoppingItems:
    if item == "Spam":
        print("Breaking at the item " + item)
        break
    print("Buy: " + item)
else:
    print("Spam was not found in List")
