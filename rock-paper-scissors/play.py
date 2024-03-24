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
    random_choice = random.choice(["rock", "paper", "scissors"])
    print(items.keys())
    user = input("[1] -> rock \n[2] -> paper \n[3] -> scissors\n ->")

    # handle invalid choice
    if user not in ["1", "2", "3"]:
        print("Invalid choice")
        return None
    
    # convert the choice into integer
    res = choose_winner(items[user]['title'], random_choice)
    (
        print("It's a Draw")
        if res == None
        else print("You Win !") if res else print("You Lose !")
    )
