import turtle
from .types import Snake, Food
from .exceptions import *
import typing
import time


class Game:
    def __init__(self, resolution: typing.Tuple = None, bgpic: str = None):
        self.snake = None
        self.pause = True
        self.foods = []
        self.level = 1
        self.window = turtle.Screen()
        self.score_pen = turtle.Turtle(visible=False)
        self.score_pen.speed(0)
        self.score_pen.goto(-400, 290)
        self.score_pen.clear()
        self.delay = 0.3
        self.score_pen.write('Уровень:' + str(self.level), font=('Arial', 15, 'normal'))
        self.tracer_n = 1
        if resolution:
            self.window.setup(resolution[0], resolution[1])
        if bgpic:
            self.window.bgpic(bgpic)

    def start(self, pause: bool = False):
        if not pause:
            self.pause = False
        self.new_snake()
        self.new_food()

    def set_level(self, new_level: int):
        self.level = new_level
        self.score_pen.clear()
        self.score_pen.write('Уровень:' + str(self.level), font=('Arial', 15, 'normal'))

    def new_food(self):
        food = Food(self)
        self.foods.append(food)

    def new_snake(self, x=None, y=None, **kwargs):
        self.snake = Snake(self, **kwargs)
        return self.snake

    def delete_snake(self):
        if not self.snake:
            raise SnakeCantBeDeleted('No snake exists')
        self.snake.delete()

    def set_pause(self):
        if self.pause:
            self.pause = False
            self.window.bgpic('game/images/background.gif')
        else:
            self.pause = True
            self.window.bgpic('game/images/pausebg.gif')

    def end(self):
        self.snake.head.color('darkred')
        for seg in self.snake.segments:
            seg.color('red')
        self.delete_snake()
        pen = turtle.Turtle()
        pen.penup()
        pen.write('GAME OVER', font=('Arial', 50, 'bold'))

    def mainloop(self):
        while True:
            self.window.update()
            self.window.listen()
            if self.pause:
                continue
            if not self.snake:
                continue
            self.snake.forward(20)
            if self.delay > 0:
                time.sleep(self.delay)
            for food in self.foods:
                distance = 20
                if self.snake.distance(food) <= distance:
                    self.snake.eat(food)
                    self.new_food()
                    self.delay -= 0.05
                    if self.delay <= 0 and self.level % 3 == 0:
                        self.tracer_n += 1
                    self.window.tracer(n=self.tracer_n)
            for seg in self.snake.segments:
                if self.snake.head.distance(seg) < 10:
                    self.end()
                    break

            pos = self.snake.head.pos()
            if pos[0] >= self.window.screensize()[0]:
                self.snake.goto(-self.window.screensize()[0], pos[1])
            if pos[1] >= self.window.screensize()[1]:
                self.snake.goto(pos[0], -self.window.screensize()[1])
            if pos[0] <= - self.window.screensize()[0]:
                self.snake.goto(self.window.screensize()[0], pos[1])
            if pos[1] <= -self.window.screensize()[1]:
                self.snake.goto(pos[0], self.window.screensize()[1])
