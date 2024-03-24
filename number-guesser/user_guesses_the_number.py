import random
def guess(guessed_num, target):
    tries = 1
    while guessed_num != target:
        tries += 1
        if guessed_num < target:
            guessed_num = int(input("Number is lower than the target. Guess again: "))
        else:
            guessed_num = int(input("Number is greater than the target. Guess again: "))
    print(f"Hooray ! You guessed the number. It was {target}. Number of tries: {tries}")


def user_guesses_the_number():
    try:
        print("Enter the range of numbers to guess: \n")
        start_num = int(input("From: "))
        end_num = int(input("To: "))

        if end_num < start_num:
            raise ValueError("Invalid range")

        print(
            f"You have to guess a number I am thinking of between {start_num} and {end_num}"
        )
        random_number = random.randint(start_num, end_num)

        guessed_num = int(input("Try Guessing the Number: "))
        guess(guessed_num, random_number)

    except Exception as err:
        print(err)