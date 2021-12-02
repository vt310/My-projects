from turtle import Screen, Turtle
segments = []


class Snake:
    def __init__(self):
        self.segments = []
        all_positions = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]

        for position in all_positions:
            self.add_segment(position)
        self.head = self.segments[0]


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto((new_x, new_y))

        self.head.forward(20)

    def up(self):
        if not self.head.heading() == 270.0:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90.0:
            self.head.setheading(270)

    def right(self):
        if not self.head.heading() == 180.0:
            self.head.setheading(0)

    def left(self):
        if not self.head.heading() == 0.0:
            self.head.setheading(180)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())



