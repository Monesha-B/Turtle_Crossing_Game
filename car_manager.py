from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
Y_DISTANCE = [-250, -200, -150,-100,-50,0,50,100,150,200,250]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_num = random.randint(1,6)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.up()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def keep_moving(self):
        for i in self.all_cars:
            i.backward(self.speed)


    def level_up(self):
        self.speed += MOVE_INCREMENT

