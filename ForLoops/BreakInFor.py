shoppingItems = ["Milk", "Bread", "Eggs", "Jam", "Apple", "Spam", "Orange", "Butter"]

unwantedItem = ''

for item in shoppingItems:
    if item == "Spam":
        print("Breaking at the item " + item)
        unwantedItem = item
        break
    print("Buy: " + item)


if unwantedItem == "Spam":
    print("Do not buy: " + unwantedItem)
