print(not True)
print(not False)

age = int(input("Please enter your age: "))

if not (age < 18):  #if you enter 12, it will be less than 18 i.e it's TRUE and we are making it FALSE using 'not'
    print("You can vote")
else:
    print("Please come back in " + str(18-age) + " years")