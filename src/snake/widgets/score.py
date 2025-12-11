import pygame

from snake.config import SCORE_POSITION


class Score:
    def __init__(self) -> None:
        self.pos = SCORE_POSITION
        self.font = pygame.font.SysFont(None, 48)

    def draw(self, score, screen: pygame.surface.Surface) -> None:
        test_surface = self.font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(test_surface, (SCORE_POSITION))
