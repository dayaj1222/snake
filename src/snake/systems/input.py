import pygame
from pygame.event import Event

from snake.config import DOWN, LEFT, RIGHT, UP


class InputHandler:
    def __init__(self, snake) -> None:
        self.snake = snake

    def handle_event(self, event: Event):
        current_direction = self.snake.head.direction

        if event.key == pygame.K_w or event.key == pygame.K_UP:
            if current_direction != DOWN:
                self.snake.head.direction = UP
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            if current_direction != UP:
                self.snake.head.direction = DOWN
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if current_direction != LEFT:
                self.snake.head.direction = RIGHT
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            if current_direction != RIGHT:
                self.snake.head.direction = LEFT
