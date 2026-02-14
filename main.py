from turtle import Screen, Turtle 
import time
from snake import my_Snake
from food import Food
  
from scoreboard import Score


screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = my_Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # detect collision with food
    
    
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()

        
        score.increase()
        snake.point()

    # detect collision with wall
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 340 or snake.head.ycor() <- 340 :
        snake.game_over_music() # music
        score.game_over()
        score.reset()
        screen.exitonclick()
    

    # detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            snake.game_over_music() # music
            score.game_over()
            score.reset()
            screen.exitonclick()




screen.exitonclick()