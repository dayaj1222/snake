import pygame

from snake.config import BG_COLOR, GameState
from snake.entities.food import Food
from snake.entities.player import Snake
from snake.widgets.score import Score


class Renderer:
    def __init__(self, screen, food: Food, snake: Snake, score: Score) -> None:
        self.screen = screen
        self.food = food
        self.snake = snake
        self.score = score

    def draw(self, state: GameState, score: int):
        match state:
            case GameState.PLAYING:
                self.food.draw(self.screen)
                self.snake.draw(self.screen)
                self.score.draw(screen=self.screen, score=score)

    def clear(self):
        self.screen.fill(BG_COLOR)

    def update(self):
        pygame.display.update()
