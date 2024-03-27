from questions import questions


class Game:
    def __init__(self) -> None:
        self.score = 0

    def ask(self, item):
        print(item["question"] + "\n")
        for option, value in item["options"].items():
            print(f"[{option}] -> {value} \n")
        chosen = input("Enter your choice: ")
        if chosen == item["correct_answer"]:
            self.score += 1

    def play(self):
        for each in questions:
            self.ask(each)
        print(f"Your Score : {self.score} / {len(questions)}")


if __name__ == "__main__":
    game = Game()
    game.play()
