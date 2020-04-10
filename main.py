from game import Game


game = Game(resolution=(1000, 600), bgpic='game/images/background.gif')
game.window.tracer(n=1)
game.start(pause=True)


game.window.onkeypress(game.set_pause, 'space')
game.window.onkeypress(game.snake.turn_up, 'Up')
game.window.onkeypress(game.snake.turn_down, 'Down')
game.window.onkeypress(game.snake.turn_right, 'Right')
game.window.onkeypress(game.snake.turn_left, 'Left')

game.mainloop()
