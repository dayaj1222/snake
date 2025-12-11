import pygame

from snake.config import HEIGHT, WIDTH, GameState


class GameOverScreen:
    def __init__(self, screen: pygame.surface.Surface):
        self.screen = screen
        self.replay_button_rect = None
        self.quit_button_rect = None

    def draw(self, score: int):
        # Semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Game Over text
        font_large = pygame.font.SysFont("Arial", 72, bold=True)
        game_over_text = font_large.render("GAME OVER", True, (255, 50, 50))
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        self.screen.blit(game_over_text, game_over_rect)

        # Score text
        font_medium = pygame.font.SysFont("Arial", 48)
        score_text = font_medium.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        self.screen.blit(score_text, score_rect)

        # Replay button
        button_width, button_height = 200, 60
        self.replay_button_rect = pygame.Rect(
            WIDTH // 2 - button_width // 2,
            HEIGHT // 2 + 60,
            button_width,
            button_height,
        )
        pygame.draw.rect(
            self.screen, (100, 200, 100), self.replay_button_rect, border_radius=10
        )
        pygame.draw.rect(
            self.screen, (255, 255, 255), self.replay_button_rect, 3, border_radius=10
        )

        font_button = pygame.font.SysFont("Arial", 36)
        replay_text = font_button.render("Replay", True, (255, 255, 255))
        replay_text_rect = replay_text.get_rect(center=self.replay_button_rect.center)
        self.screen.blit(replay_text, replay_text_rect)

        # Quit button
        self.quit_button_rect = pygame.Rect(
            WIDTH // 2 - button_width // 2,
            HEIGHT // 2 + 140,
            button_width,
            button_height,
        )
        pygame.draw.rect(
            self.screen, (200, 100, 100), self.quit_button_rect, border_radius=10
        )
        pygame.draw.rect(
            self.screen, (255, 255, 255), self.quit_button_rect, 3, border_radius=10
        )

        quit_text = font_button.render("Quit", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect(center=self.quit_button_rect.center)
        self.screen.blit(quit_text, quit_text_rect)

    def handle_click(self, mouse_pos) -> GameState | None:
        if self.replay_button_rect and self.replay_button_rect.collidepoint(mouse_pos):
            return GameState.PLAYING
        elif self.quit_button_rect and self.quit_button_rect.collidepoint(mouse_pos):
            return GameState.EXIT
        return None

    def is_hovering(self, mouse_pos) -> bool:
        if self.replay_button_rect and self.replay_button_rect.collidepoint(mouse_pos):
            return True
        if self.quit_button_rect and self.quit_button_rect.collidepoint(mouse_pos):
            return True
        return False
