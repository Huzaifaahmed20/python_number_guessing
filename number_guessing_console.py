import random

random_number = random.randint(0, 999)
attempts = 3

print(random_number)

while attempts != 0:
    guessed_number = input("Please guess a number:\n")
    guessed_number = int(guessed_number)

    if (guessed_number == random_number):
        print("Horray you just got it Right!")
        attempts = 0
    else:
        print("You got it wrong :(")

        if (guessed_number > random_number):
            print("Your guess number is greater than lucky number")
        else:
            print("Your guess number is less than lucky number")

        attempts -= 1
        if (attempts == 0):
            print("No attempts left, try again later")
