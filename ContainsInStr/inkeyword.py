p = "Hello"

word = str(input("Pease enter a character: "))

if word.lower() in p.lower():
    print("The character is present")
else:
    print("The character is not present")