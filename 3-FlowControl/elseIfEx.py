
guess = int(input("Guess a number between 1 and 10: \n"))


if guess < 5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("You guess corret")
    else:
        print("You have not guessed correctly")
elif guess > 5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("You guessed it")
    else:
        print("You have not guess correctly")
else:
    print("You got it the first time")

