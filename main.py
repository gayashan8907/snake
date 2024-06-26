from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor('red')
screen.title('My Snake Game')

snake = Snake()
food = Food()
board = ScoreBoard()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    if snake.head.distance(food) <15:
        board.increase_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        board.game_over()
        game_on = False

    for segm in snake.segments[1:]:

        if snake.head.distance(segm) < 10:
            board.game_over()
            game_on = False































screen.exitonclick()