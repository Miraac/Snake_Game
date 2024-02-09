from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.draw_snake()
        self.snake_head = self.snake_segments[0]
        self.score = 0

    def draw_snake(self):
        for y_coord in range(0, -60, -20):
            segment = Turtle(shape='square')
            segment.penup()
            segment.color('white')
            segment.setposition(y_coord, 0)
            self.snake_segments.append(segment)

    def move(self):
        for segment_i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_i - 1].xcor()
            new_y = self.snake_segments[segment_i - 1].ycor()
            self.snake_segments[segment_i].goto(new_x, new_y)
        self.snake_head.forward(DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def new_segment(self):
        last_seg_position = self.snake_segments[-1].position()
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(last_seg_position)
        self.snake_segments.append(new_segment)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color('white')
        self.add_point()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f'score {self.score}', align=ALIGNMENT, font=FONT)

    def game_over_text(self):
        self.goto(0, 0)
        self.write('GAME OVER!!!', align=ALIGNMENT, font=FONT)
