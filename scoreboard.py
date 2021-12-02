from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0

    def write_text(self, new_score):
        super().ht()
        super().penup()
        super().goto((0.0, 280.0))
        super().color("white")
        super().write(f"Score:{new_score} ", move=False, align="left",font=("Courier", 15, "normal"))
        super().ht()

    def game_over(self):
        self.ht()
        self.penup()
        self.color("white")
        self.goto((0.0, 0.0))
        self.write("GAME OVER", move=False, align = "center",font=("Courier", 15, "normal"))
        self.ht()


