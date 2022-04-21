p = "Hello"

word = str(input("Enter: "))

if word.lower() not in p.lower():
    print("Not present in the word")
else:
    print("Present in word")