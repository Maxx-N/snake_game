from turtle import Turtle

import helpers
import helpers as h
from constants import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.is_bonus = False
        self.shape("circle")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.speed("fastest")
        self.penup()
        self.color(helpers.pick_random_color())

    def appear_at_random_position(self, snake):
        self.hideturtle()
        self.setposition(h.pick_random_position_out_of_snake(snake))
        self.showturtle()

    def got_eaten(self, snake):
        return self.distance(snake.head) < 15
