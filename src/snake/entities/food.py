import random
from typing import Tuple

import pygame
from pygame.sprite import Group, Sprite

from snake.config import GRID_DIM, IMAGE_DIR


class Food(Sprite):
    def __init__(
        self, *groups: Group, pos: Tuple[int, int], boundary: Tuple[int, int]
    ) -> None:
        super().__init__(*groups)
        self.pos = pos
        self.boundary = boundary

        # Internal States
        image = pygame.image.load(IMAGE_DIR / "food.png").convert_alpha()
        self.image = pygame.transform.scale(image, (GRID_DIM, GRID_DIM))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self) -> None:
        self.pos = (
            random.randint(0, self.boundary[0]),
            random.randint(0, self.boundary[1]),
        )
        self.rect.topleft = self.pos
