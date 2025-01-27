from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.up()
        self.go_to_start()
        self.setheading(90)


    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def movement_pace(self):
        # change when required
        self.forward(MOVE_DISTANCE)

    def is_player_reached(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


