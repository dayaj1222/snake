from snake.entities.food import Food
from snake.entities.player import Snake


class Renderer:
    def __init__(self, screen, food: Food, snake: Snake) -> None:
        self.screen = screen
        self.food = food
        self.snake = snake

    def add(self):
        self.food.add()

    def draw(self):
        self.food.draw(self.screen)
        self.snake.draw(self.screen)

    def update(self):
        pass
