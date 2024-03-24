import random


def computer_guesses_the_number():
    try:
        print("Give me a range of the numbers:")
        start_num = int(input("From: "))
        end_num = int(input("To:"))
        feedback = "N"
        while feedback != "y":
            if end_num < start_num:
                raise ValueError("\nInvalid Range.")
            guessed_number = random.randint(start_num, end_num)
            print(f"\nMy guess is {guessed_number}")
            feedback = input(
                "\nPress 'Y' if correct. 'H' if it is higher than the target and 'L' if lower: "
            ).lower()
            if feedback == "h":
                end_num = guessed_number - 1
                continue
            elif feedback == "l":
                start_num = guessed_number + 1
                continue
            elif feedback != "y":
                print(
                    "\nEnter either 'H' if guessed number is higher than target or 'L' if lower."
                )
                continue
            print(f"So the Number was {guessed_number}. Nice guess xd. ")

    except Exception as err:
        print(err)
