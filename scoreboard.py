from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.init_high_score()
        self.update_score()

    def init_high_score(self):
        with open("high_score.txt") as file:
            h = file.readline()
            if h:
                self.high_score = int(h)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
