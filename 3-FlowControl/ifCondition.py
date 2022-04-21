name = "Mr"#input("Please enter your name: ")
age = int(input("How old are you, {0} ".format(name)))
print(age)


if age >= 18:
    print("You can VOTE")
    print("Please put an X in the box")
else:
    print("You cannot Vote, please come back in " + str(18-age)+" years")
