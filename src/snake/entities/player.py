import pygame
from pygame.math import Vector2
from pygame.sprite import Group, Sprite

from snake.config import DOWN, GRID_DIM, HEIGHT, IMAGE_DIR, LEFT, RIGHT, UP, WIDTH


class Head(Sprite):
    def __init__(
        self,
        *groups: Group,
        direction: Vector2 = RIGHT,
        pos: Vector2 = Vector2(GRID_DIM * 2, 0),
    ) -> None:
        super().__init__(*groups)
        self.direction = direction
        self.pos = pos
        self.num = 0
        self.position_stack = []

        # Internal states
        self.image = pygame.Surface((GRID_DIM, GRID_DIM))
        pygame.draw.rect(self.image, (0, 0, 255), (4, 4, 24, 24))
        self.rect = self.image.get_rect()

    def update(self) -> None:

        self.rect.topleft = (int(self.pos.x), int(self.pos.y))


class Block(Sprite):
    def __init__(
        self,
        *groups: Group,
        pos: Vector2 = Vector2(0, 0),
        num: int = 1,
        direction: Vector2 = RIGHT,
    ) -> None:
        super().__init__(*groups)
        self.pos = pos
        self.num = num

        # Internal states
        self.image = pygame.Surface((GRID_DIM, GRID_DIM))
        pygame.draw.rect(self.image, (0, 255, 0), (4, 4, 24, 24))
        self.rect = self.image.get_rect()

    def update(self) -> None:
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))


class Snake:
    def __init__(self, head: Head, body: Block):
        self.head = head
        self.body = body
        self.pieces: list = [head, body]

    def grow(self):
        new_part = Block(pos=self.pieces[-1].pos, num=len(self.pieces))
        new_part.update()
        self.pieces.append(new_part)

    def draw(self, screen: pygame.surface.Surface):
        for piece in self.pieces:
            screen.blit(piece.image, (piece.rect))

    def move(self):
        prev_positions = [piece.pos.copy() for piece in self.pieces]
        self.head.pos += self.head.direction * GRID_DIM
        for i in range(1, len(self.pieces)):
            self.pieces[i].pos = prev_positions[i - 1]
        for piece in self.pieces:
            piece.update()
