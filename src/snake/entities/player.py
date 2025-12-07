import select
from enum import Enum
from typing import Tuple

import pygame
from pygame import display
from pygame.sprite import Group, Sprite

from snake.config import GRID_DIM, HEIGHT, IMAGE_DIR, WIDTH


class Snake:
    def __init__(self, head: Sprite, body: list[Sprite]):
        self.head = head
        self.body = body

    def render(self):
        pass


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Head(Sprite):
    def __init__(
        self,
        *groups: Group,
        direction: Direction = Direction.RIGHT,
        pos: Tuple[int, int] = (int(WIDTH / 2), int(HEIGHT / 2)),
    ) -> None:
        super().__init__(*groups)
        self.direction = direction
        self.pos = pos

        # Internal states
        image = pygame.image.load(IMAGE_DIR / "snake_head.png").convert_alpha()
        self.image = pygame.transform.scale(image, (GRID_DIM, GRID_DIM))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self) -> None:
        match self.direction:
            case Direction.UP:
                self.pos = (self.pos[0], self.pos[1] - GRID_DIM)
            case Direction.DOWN:
                self.pos = (self.pos[0], self.pos[1] + GRID_DIM)
            case Direction.LEFT:
                self.pos = (self.pos[0] - GRID_DIM, self.pos[1])
            case Direction.RIGHT:
                self.pos = (self.pos[0] + GRID_DIM, self.pos[1])

        self.rect.topleft = self.pos
