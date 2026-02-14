from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.score = -1
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.increase()
    def increase(self):
        self.score+=1
        self.update_score()
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
    
    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.highscore}", align="center" , font= ("lethal", 24, "normal") )

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"game is over", align="center" , font= ("Arial", 50, "normal") )

        