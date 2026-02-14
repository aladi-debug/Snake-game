from turtle import Screen, Turtle
import pygame
STARTING_POSITIONS = [(0, 0),(-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
pygame.mixer.init()


class my_Snake:
    def __init__(self):
        
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        

 
    def create_snake(self):
        
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


                
    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
            for seg_num in range(len(self.segments)-1, 0 , -1):
                new_x = self.segments[seg_num-1].xcor()
                new_y = self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x, new_y)

            self.head.forward(MOVE_DISTANCE)
    def up(self):
       if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.turn_music()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.turn_music()
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.turn_music()
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.turn_music()
    def game_over_music(self):
        pygame.mixer.init()
        pygame.mixer.Sound("game-over.wav").play()
    
    def reset_snake(self):
        for snake in self.segments:
            snake.color("black")
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def point(self):
        pygame.mixer.init()
        pygame.mixer.Sound("point.wav").play()

    def turn_music(self):
        pygame.mixer.init()
        pygame.mixer.Sound("woosh.wav").play()
    


         