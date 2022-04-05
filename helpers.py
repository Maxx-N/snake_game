import random
import time
from turtle import Turtle, Screen

from constants import *


def define_sleep_time(score):
    if score < 10:
        return SLEEP_TIME
    elif score < 20:
        return SLEEP_TIME - .01
    elif score < 30:
        return SLEEP_TIME - .02
    elif score < 40:
        return SLEEP_TIME - .03
    elif score < 50:
        return SLEEP_TIME - .04
    else:
        return SLEEP_TIME - .05


def write_score(score):
    drawer = Turtle()
    drawer.hideturtle()
    drawer.penup()
    drawer.color(TEXT_COLOR)
    drawer.setposition(LIMIT_RIGHT - 4 * SCORE_SIZE, LIMIT_TOP - 4 * SCORE_SIZE)
    drawer.write(arg=score, move=False, align="left", font=("normal", SCORE_SIZE, "bold"))
    return drawer


def pick_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def pick_random_position_out_of_snake(snake):
    x = random.randint(LIMIT_LEFT + 10, LIMIT_RIGHT - 10)
    y = random.randint(LIMIT_BOTTOM + 10, LIMIT_TOP - 10)
    while (x, y) in snake.get_cells_positions():
        x = random.randint(LIMIT_LEFT + 10, LIMIT_RIGHT - 10)
        y = random.randint(LIMIT_BOTTOM + 10, LIMIT_TOP - 10)
    return x, y


def define_screen():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_COLOR)
    screen.title("Snake")
    screen.tracer(0)
    return screen


def draw_text(title, text, size, color):
    drawer = Turtle()
    drawer.hideturtle()
    drawer.color(color)
    drawer.write(arg=title, move=False, align="center", font=("normal", size, "bold"))
    drawer.sety(drawer.xcor() - size * 2)
    drawer.write(arg=text, move=False, align="center", font=("normal", int(size / 2), "bold"))


def draw_screen_limits(screen):
    drawer = Turtle()
    drawer.hideturtle()
    drawer.color(BORDER_COLOR)
    drawer.penup()
    drawer.goto((LIMIT_RIGHT, LIMIT_TOP))
    drawer.pendown()
    drawer.goto((LIMIT_RIGHT, LIMIT_BOTTOM))
    drawer.goto((LIMIT_LEFT, LIMIT_BOTTOM))
    drawer.goto((LIMIT_LEFT, LIMIT_TOP))
    drawer.goto((LIMIT_RIGHT, LIMIT_TOP))


def configure_keys(snake):
    snake.screen.listen()
    snake.screen.onkey(key="Up", fun=snake.move_up)
    snake.screen.onkey(key="Down", fun=snake.move_down)
    snake.screen.onkey(key="Left", fun=snake.move_left)
    snake.screen.onkey(key="Right", fun=snake.move_right)


def display(screen, delay):
    screen.update()
    time.sleep(delay)


def create_snake_body(full_size, speed):
    body = []
    x = 0
    for _ in range(full_size):
        new_piece = create_piece_of_snake(position=(x, 0), speed=speed, color=SNAKE_INITIAL_COLOR)
        body.append(new_piece)
        x -= 20
    return body


def create_piece_of_snake(position, speed, color):
    new_cell = Turtle()
    new_cell.shape("square")
    new_cell.color(color)
    new_cell.penup()
    new_cell.setposition(position)
    new_cell.speed(speed)
    return new_cell


def convert_float_tuple_to_int_tuple(float_tuple):
    if isinstance(float_tuple, tuple):
        return int(float_tuple[0]), int(float_tuple[1]), int(float_tuple[2])
    else:
        return float_tuple
