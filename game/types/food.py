import turtle
import random


class Food(turtle.Turtle):
    def __init__(self, game, x: int = None, y: int = None, visible: bool = True, **kwargs):
        """
        Food for the Snake
        :param x: x-coord where to appear, if None, it's chosen randomly
        :param y: y-coord where to appear, if None, it's chosen randomly
        :param visible: if the Snake should be visible when appears
        """
        super().__init__(visible=False, **kwargs)
        self.penup()
        if not x:
            x = random.randint(-300, 300)
        if not y:
            y = random.randint(-300, 300)
        self.goto(x, y)
        self.shape(random.choice(('circle', 'square')))
        self.game = game
        if visible:
            self.showturtle()

    def delete(self):
        self.clear()
        self.reset()
        del self.game.foods[self.game.foods.index(self)]
        self.hideturtle()
