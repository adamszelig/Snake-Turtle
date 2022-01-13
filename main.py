from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

REFRESH_TIME = 0.05
EAT = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Tornado")
screen.tracer(0)

snake = Snake()
food = Food()
points = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
#print(snake.ninjas[0].xcor())
points.init_high_score()
while game:
    screen.update()
    time.sleep(REFRESH_TIME)
    snake.move()

    # Detect collision
    if snake.ninjas[0].distance(food) < 15:
        food.refresh()
        points.increase_score()
        for _ in range(EAT):
            snake.extend()

    # Detect collision with wall
    if snake.ninjas[0].xcor() > 280 or snake.ninjas[0].xcor() < -280 \
            or snake.ninjas[0].ycor() > 280 or snake.ninjas[0].ycor() < -280:
        points.reset()
        snake.reset()

    # Detect collision with tail
    # for ninja in snake.ninjas:
    #     if ninja == snake.ninjas[0]:
    #         pass
    #     elif snake.ninjas[0].distance(ninja) < 8:
    #         game = False
    #         points.game_over()

    for ninja in snake.ninjas[1:]:
        if snake.ninjas[0].distance(ninja) < 8:
            points.reset()
            snake.reset()


screen.exitonclick()
