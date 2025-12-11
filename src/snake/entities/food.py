import random

import pygame
from pygame import Vector2
from pygame.sprite import Group, Sprite

from snake.config import GRID_DIM, HEIGHT_BLOCKS, IMAGE_DIR, WIDTH_BLOCKS


class Food(Sprite):
    def __init__(self, *groups: Group, pos: Vector2) -> None:
        super().__init__(*groups)
        self.pos = pos

        # Internal States
        image = pygame.image.load(IMAGE_DIR / "food.png").convert_alpha()
        self.image = pygame.transform.scale(image, (GRID_DIM, GRID_DIM))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self) -> None:
        self.pos = (
            random.randint(0, WIDTH_BLOCKS - 1) * GRID_DIM,
            random.randint(0, HEIGHT_BLOCKS - 1) * GRID_DIM,
        )
        self.rect.topleft = self.pos

    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.pos)
