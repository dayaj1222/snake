import pygame
from pygame.sprite import Group, Sprite

from snake.entities.food import Food


class Renderer:
    def __init__(self, screen, entities: list) -> None:
        self.screen = screen
        self.sprites = Group()
        self.entities = entities

    def add(self):
        for entity in self.entities:
            self.sprites.add(entity)

    def draw(self):
        self.sprites.draw(self.screen)

    def update(self):
        pass
