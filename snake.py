from turtle import Turtle
INIT_POS = [0, 0]
MOVE_DISTANCE = 10
# STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0), (-30, 0), (-40, 0), (-50, 0)]


class Snake:
    def __init__(self):
        self.ninjas = []
        self.create_ninja()

    def create_ninja(self):
        for pos in STARTING_POSITION:
            self.add_ninja(pos)

    def add_ninja(self, position):
        self.ninja = Turtle()
        self.ninja.shape("square")
        self.ninja.color("white")
        self.ninja.penup()
        self.ninja.goto(position)
        self.ninjas.append(self.ninja)

    def extend(self):
        self.add_ninja(self.ninjas[-1].position())

    def move(self):
        for i in range(len(self.ninjas) - 1, 0, -1):
            new_x = self.ninjas[i - 1].xcor()
            new_y = self.ninjas[i - 1].ycor()
            self.ninjas[i].setpos(x=new_x, y=new_y)
        self.ninjas[0].forward(MOVE_DISTANCE)

    def reset(self):
            for ninja in self.ninjas:
                ninja.goto(1000, 1000)
            self.ninjas.clear()
            self.create_ninja()

    def up(self):
        if self.ninjas[0].heading() != 270:
            self.ninjas[0].setheading(90)

    def down(self):
        if self.ninjas[0].heading() != 90:
            self.ninjas[0].setheading(270)

    def left(self):
        if self.ninjas[0].heading() != 0:
            self.ninjas[0].setheading(180)

    def right(self):
        if self.ninjas[0].heading() != 180:
            self.ninjas[0].setheading(0)
