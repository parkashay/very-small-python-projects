from user_guesses_the_number import user_guesses_the_number
from computer_guesses_the_number import computer_guesses_the_number

if __name__ == "__main__":
    game_type = int(
        input(
            "Enter 1 if you want to guess the number \nEnter 2 if you want the computer to guess the number.\n ->"
        )
    )
    if game_type == 1:
        user_guesses_the_number()
    elif game_type == 2:
        computer_guesses_the_number()
    else:
        print("Choose from either 1 or 2.")
        exit()
