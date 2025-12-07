import pygame
from pygame.math import Vector2
from pygame.sprite import Group, Sprite

from snake.config import DOWN, GRID_DIM, HEIGHT, IMAGE_DIR, LEFT, RIGHT, UP, WIDTH


class Snake:
    def __init__(self, head: Sprite, length: int):
        pass


class Head(Sprite):
    def __init__(
        self,
        *groups: Group,
        direction: Vector2 = RIGHT,
        pos: Vector2 = Vector2(int(WIDTH / 2), int(HEIGHT / 2)),
    ) -> None:
        super().__init__(*groups)
        self.direction = direction
        self.pos = pos
        self.num = 0
        self.position_stack = []

        # Internal states
        image = pygame.image.load(IMAGE_DIR / "snake_head.png").convert_alpha()
        self.image = pygame.transform.scale(image, (GRID_DIM, GRID_DIM))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self) -> None:

        self.rect.topleft = (int(self.pos.x), int(self.pos.y))


class Block(Sprite):
    def __init__(
        self, *groups: Group, pos: Vector2, num: int, direction: Vector2 = RIGHT
    ) -> None:
        super().__init__(*groups)
        self.pos = pos
        self.direction = direction
        self.num = num

        # Internal states
        image = pygame.image.load(IMAGE_DIR / "body_block.png").convert_alpha()
        self.image = pygame.transform.scale(image, (GRID_DIM, GRID_DIM))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, f_pos: Vector2) -> None:
        self.pos = f_pos
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))
