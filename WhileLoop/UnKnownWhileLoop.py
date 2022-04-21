directions = ["east", "west", "north", "south"]

way = input("Enter a direction: ")

while way not in directions:
    way = input("Please enter again: ")
    if way == "exit":
        print("You lost")
        break
else:
    print("This Line will execute only if the 'break statement' does get executed")