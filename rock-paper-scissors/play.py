import random
from icons import rock, paper, scissors


def choose_winner(p1, computer):
    if p1 == computer:
        return None
    return (
        (p1 == "paper" and computer == "rock")
        or (p1 == "scissors" and computer == "paper")
        or (p1 == "rock" and computer == "scissors")
    )


def play():
    items = {"1": rock, "2": paper, "3": scissors}
    choices = ["1", "2", "3"]
    user = input("[1] -> rock \n[2] -> paper \n[3] -> scissors\n -> ")

    # handle invalid choice
    if user not in choices:
        print("Invalid choice")
        return None

    random_choice = random.choice(choices)
    print("You:", items[user]["symbol"], "\nComputer:", items[random_choice]["symbol"])
    # choose the winner
    res = choose_winner(
        items[user]["title"].lower(), items[random_choice]["title"].lower()
    )
    (
        print("It's a Draw")
        if res == None
        else print("You Win !") if res else print("You Lose !")
    )
