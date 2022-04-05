import datetime as dt
import random
from turtle import Turtle

import helpers as h
from constants import *
from models.food import Food


class Bonus(Food):
    def __init__(self):
        super().__init__()
        self.is_bonus = True
        self.setheading(90)
        self.hideturtle()
        self.exists = False
        self.value = 0
        self.duration = 0
        self.drawer = Turtle()
        self.drawer.penup()
        self.drawer.hideturtle()
        self.drawer.setposition(LIMIT_LEFT + 4 * SCORE_SIZE, LIMIT_TOP - 4 * SCORE_SIZE)

    def randomly_appear(self, snake):
        number = random.randint(1, BONUS_PROBABILITY)
        if number == 1:
            self.appear_at_random_position(snake)

    def appear_at_random_position(self, snake):
        self.value = random.choice([SQUARE_BONUS_VALUE, TRIANGLE_BONUS_VALUE, TURTLE_BONUS_VALUE])
        if self.value == SQUARE_BONUS_VALUE:
            self.shape("square")
            self.duration = SQUARE_BONUS_DURATION
        elif self.value == TRIANGLE_BONUS_VALUE:
            self.shape("triangle")
            self.duration = TRIANGLE_BONUS_DURATION
        else:
            self.shape("turtle")
            self.duration = TURTLE_BONUS_DURATION
        self.setposition(h.pick_random_position_out_of_snake(snake))
        self.exists = True
        self.showturtle()
        self.start_time = dt.datetime.now()

    def is_expired(self):
        date_after_duration = self.start_time + dt.timedelta(seconds=self.duration)
        return dt.datetime.now() >= date_after_duration

    def blink(self):
        if self.exists:
            if self.pencolor() == SCREEN_COLOR:
                self.color(h.pick_random_color())
            else:
                self.color(SCREEN_COLOR)

    def disappear(self):
        self.exists = False
        self.hideturtle()
        self.duration = 0
        self.value = 0
        self.drawer.clear()

    def display_countdown(self):
        if self.exists:
            expiration_date = self.start_time + dt.timedelta(seconds=self.duration)
            remaining_time = expiration_date - dt.datetime.now()
            remaining_seconds = int(remaining_time.total_seconds())
            self.drawer.clear()
            self.drawer.color(h.pick_random_color())
            self.drawer.write(arg=remaining_seconds, move=False, align="right", font=("normal", SCORE_SIZE, "normal"))
