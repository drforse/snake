from game import Game


game = Game(resolution=(800, 600), bgpic='game/images/background.gif')
game.start(pause=True)


game.window.onkeypress(game.set_pause, 'space')
game.window.onkeypress(game.snake.turn_up, 'Up')
game.window.onkeypress(game.snake.turn_down, 'Down')
game.window.onkeypress(game.snake.turn_right, 'Right')
game.window.onkeypress(game.snake.turn_left, 'Left')

game.mainloop()
