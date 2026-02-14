import turtle 
import random


turtle.colormode(255)


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
       
        self.refresh()

    def refresh(self):
        random_x = random.randint(-480,480)
        random_y = random.randint(-320,320)
        self.goto(random_x, random_y)



