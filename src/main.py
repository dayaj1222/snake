import pygame

from snake.config import BG_COLOR, FPS, HEIGHT, WIDTH
from snake.entities.food import Food
from snake.systems.renderer import Renderer


def main():
    # Constants

    # Game state
    RUNNING = True

    # Initialize pygame
    pygame.init()

    # Create main Window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    # Create Clock
    clock = pygame.time.Clock()

    # Create Renderer
    sprites = pygame.sprite.Group()
    food = Food(sprites, pos=(200, 400), boundary=(WIDTH, HEIGHT))

    # Main Loop
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                pass

        screen.fill(BG_COLOR)
        clock.tick(FPS)

        # Render Everything else:
        renderer = Renderer(screen, [food])
        renderer.add()
        renderer.draw()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
