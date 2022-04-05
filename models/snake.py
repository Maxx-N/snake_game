import helpers as h
from constants import *


class Snake:
    def __init__(self, screen, size=3, speed=1):
        self.speed = speed
        self.body = h.create_snake_body(size, speed)
        self.head = self.body[0]
        self.screen = screen
        self.is_alive = True
        self.score = 0

    def eat(self, food):
        if food.is_bonus:
            self.change_color(SNAKE_INITIAL_COLOR)
            self.score += food.value
        else:
            self.change_color(food.pencolor())
            self.score += 1
            self.grow_up()

    def grow_up(self):
        for _ in range(GROW_UP_BY):
            new_cell = h.create_piece_of_snake(position=self.body[-1].position(), speed=self.head.speed(),
                                               color=h.convert_float_tuple_to_int_tuple(self.head.pencolor()))
            self.body.append(new_cell)

    def move_forward(self):
        for index in range(len(self.body) - 1, -1, -1):
            if index == 0:
                self.head.forward(20)
                self.cross_screen_if_wall()
            else:
                self.body[index].setposition(self.body[index - 1].position())

    def move_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)
            self.move_forward()

    def move_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)
            self.move_forward()

    def move_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
            self.move_forward()

    def move_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
            self.move_forward()

    def cross_screen_if_wall(self):
        if self.has_reached_right_wall():
            self.head.setx(LIMIT_LEFT + 10)
        if self.has_reached_left_wall():
            self.head.setx(LIMIT_RIGHT - 10)
        if self.has_reached_top_wall():
            self.head.sety(LIMIT_BOTTOM + 10)
        if self.has_reached_bottom_wall():
            self.head.sety(LIMIT_TOP - 10)

    def has_reached_right_wall(self):
        return self.head.xcor() >= LIMIT_RIGHT and self.head.heading() == RIGHT

    def has_reached_left_wall(self):
        return self.head.xcor() <= LIMIT_LEFT and self.head.heading() == LEFT

    def has_reached_top_wall(self):
        return self.head.ycor() >= LIMIT_TOP and self.head.heading() == UP

    def has_reached_bottom_wall(self):
        return self.head.ycor() <= LIMIT_BOTTOM and self.head.heading() == DOWN

    def change_color(self, color):
        for cell in self.body:
            cell.color(h.convert_float_tuple_to_int_tuple(color))

    def get_tail_cells(self):
        # tail_cells = []
        #     for index in range(1, len(self.body)):
        #         tail_cells.append(self.body[index])
        #     return tail_cells
        return self.body[1:]

    def is_self_collision(self):
        collision = False
        for cell in self.get_tail_cells():
            if self.head.distance(cell) <= 10:
                collision = True
                break
        return collision

    def blink(self, screen, times):
        for _ in range(times):
            for cell in self.body:
                cell.hideturtle()
            h.display(screen=screen, delay=SLEEP_TIME)
            for cell in self.body:
                cell.showturtle()
            h.display(screen=screen, delay=SLEEP_TIME)

    def get_cells_positions(self):
        positions = []
        for cell in self.body:
            for horizontal in range(-9, 10):
                x = cell.xcor() + horizontal
                for vertical in range(-9, 10):
                    y = cell.ycor() + vertical
                    positions.append((x, y))
        return positions

    # def turn_anti_clockwise(self):
    #     self.head.setheading(self.head.heading() + 90)
    #     self.move_forward()
    #
    # def turn_clockwise(self):
    #     self.head.setheading(self.body[0].heading() - 90)
    #     self.move_forward()

    # def move_forward(self):
    #     self.body[0].forward(20)
    #     previous_original_heading = self.body[0].heading()
    #     for index in range(1, len(self.body)):
    #         cell = self.body[index]
    #         cell.forward(20)
    #         if not cell.heading() == previous_original_heading:
    #             current_original_heading = cell.heading()
    #             cell.setheading(previous_original_heading)
    #             previous_original_heading = current_original_heading
