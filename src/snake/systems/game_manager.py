import sys
from enum import Enum

from snake.config import HEIGHT, WIDTH, GameState
from snake.entities.food import Food
from snake.entities.player import Snake
from snake.systems.renderer import Renderer


class GameManager:
    def __init__(self, snake: Snake, food: Food, renderer: Renderer):
        self.snake = snake
        self.food = food
        self.renderer = renderer
        self.state: GameState = GameState.PLAYING
        self.score: int = 0

    def check_collosion(self):
        if self.snake.head.pos == self.food.pos:
            self.score += 1
            self.food.update()
            self.snake.grow()
        for piece in self.snake.pieces[1:]:
            if self.snake.head.pos == piece.pos:
                self.state = GameState.GAME_OVER

    def check_state(self):
        match self.state:
            case GameState.PLAYING:
                pass
            case GameState.GAME_OVER:
                sys.exit()

    def print_score(self):
        print("Game Over, Score: ", self.score)
