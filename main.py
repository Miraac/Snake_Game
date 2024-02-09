from turtle import Screen
import time
from snake_classes import Snake, Score
from food import Food

screen = Screen()
screen.screensize(600, 600, bg='black')
print(f'expect screen size: {screen.screensize()}')
screen.title('Snake V1 by Mirac')
screen.tracer(0)

# objects
# start snake with 3 segments
snake = Snake()
food = Food()
score = Score()


# move listener
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    # eat food
    if snake.snake_head.distance(food) < 15:
        print('om nom nom')
        food.new_food()
        score.add_point()
        snake.new_segment()

    # wall collision
    if (snake.snake_head.xcor() > 300 or
            snake.snake_head.xcor() < -300 or
            snake.snake_head.ycor() > 300 or
            snake.snake_head.ycor() < -300):
        score.game_over_text()
        game_is_on = False

    # tail collision
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score.game_over_text()
screen.exitonclick()
