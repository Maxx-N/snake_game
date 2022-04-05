import turtle

from helpers import *
from models.bonus import Bonus
from models.food import Food
from models.snake import Snake

turtle.colormode(255)

screen = define_screen()


def process():
    display(screen=screen, delay=SLEEP_TIME)
    draw_screen_limits(screen)
    snake = Snake(screen=screen, size=3)
    food = Food()
    food.appear_at_random_position(snake)
    configure_keys(snake=snake)
    bonus = Bonus()
    score_drawer = write_score(score=snake.score)
    while snake.is_alive:
        display(screen=screen, delay=define_sleep_time(snake.score))
        bonus.blink()
        bonus.display_countdown()
        if bonus.exists:
            if bonus.got_eaten(snake):
                snake.eat(bonus)
                bonus.disappear()
                score_drawer.clear()
                score_drawer = write_score(score=snake.score)
                snake.blink(screen, 2)
            if bonus.is_expired():
                bonus.disappear()
        if food.got_eaten(snake):
            if not bonus.exists:
                bonus.randomly_appear(snake=snake)
            snake.eat(food)
            food.appear_at_random_position(snake)
            food.color(pick_random_color())
            score_drawer.clear()
            score_drawer = write_score(score=snake.score)
        if snake.is_self_collision() or snake.has_reached_bottom_wall():
            snake.is_alive = False
            snake.blink(screen=screen, times=5)
        snake.move_forward()

    draw_text(title="GAME OVER", text=f"Your final score is: {snake.score}", size=50,
              color=convert_float_tuple_to_int_tuple(food.pencolor()))


process()
screen.exitonclick()
