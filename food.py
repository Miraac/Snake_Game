from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("yellow")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        food_x = randint(-14, 14) * 20
        food_y = randint(-14, 14) * 20
        self.goto(food_x, food_y)
        print(f'food coord: {food_x},{food_y}')
