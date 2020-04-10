import turtle
from ..exceptions import *
import gc
import typing
import copy
import builtins


class Snake:
    def __init__(self, game, x: int = 0, y: int = 0, visible: bool = True, **kwargs):
        """
        the Snake
        :param x: x-coord of where the snake should appear
        :param y: y-coord of where the snake should appear
        :param visible: if the Snake should be visible when appears
        """
        if game.snake:
            SnakeCantBeCreated('Only one snake can exist')
        self.head = SnakeSegment(x=x, y=y, visible=visible, color='white', **kwargs)
        self.last_state = {}
        self.game = game
        self.segments: typing.List[turtle.Turtle] = []

    def forward(self, distance: int):
        self.last_state = {'head': {'position': self.head.position(),
                                    'heading': self.head.heading()},
                           'segments': [{'position': seg.position(),
                                         'heading': seg.heading()}
                                        for seg in self.segments]}
        self.head.forward(distance)
        for num, segment in enumerate(self.segments):
            if num == 0:
                x = self.last_state['head']['position'][0]
                y = self.last_state['head']['position'][1]
            else:
                x = self.last_state['segments'][num-1]['position'][0]
                y = self.last_state['segments'][num-1]['position'][1]
            segment.goto(x, y)

    def distance(self, x=None, y=None):
        return self.head.distance(x=x, y=y)

    def turn_up(self):
        self.head.setheading(90)

    def turn_down(self):
        self.head.setheading(-90)

    def turn_right(self):
        self.head.setheading(360)

    def turn_left(self):
        self.head.setheading(180)

    def delete(self):
        for seg in self.segments:
            seg.clear()
            self.game.snake = None

    def add_segment(self):
        if not self.segments:
            x = self.last_state['head']['position'][0]
            y = self.last_state['head']['position'][1]
            heading = self.last_state['head']['heading']
        else:
            x = self.last_state['segments'][-1]['position'][0]
            y = self.last_state['segments'][-1]['position'][1]
            heading = self.last_state['segments'][-1]['heading']
        self.segments.append(SnakeSegment(x=x, y=y, heading=heading, speed=0))

    def eat(self, food):
        food.delete()
        del food
        gc.collect()
        self.add_segment()
        self.game.set_level(self.game.level + 1)


class SnakeSegment(turtle.Turtle):
    def __init__(self, x: int = 0, y: int = 0, heading: int = 90,
                 visible: bool = True, color: str = 'violet', speed: int = 1, **kwargs):
        super().__init__(visible=False, **kwargs)
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.setheading(heading)
        self.shape('square')
        if visible:
            self.showturtle()
