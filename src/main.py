from xxlimited import foo

import pygame
from pygame import Vector2

from snake.config import BG_COLOR, FPS, HEIGHT, RENDER_DELAY, WIDTH
from snake.entities.food import Food
from snake.entities.player import Block, Head, Snake
from snake.systems.game_manager import GameManager
from snake.systems.input import InputHandler
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

    # Initialize Game Objects
    food = Food(pos=Vector2(200, 400))
    head = Head()
    body = Block()
    snake = Snake(
        head,
        body,
    )

    # Initialize Input Handler
    input_handler = InputHandler(snake)

    # Initialize GameManager

    game_manager = GameManager(snake=snake, food=food, renderer=renderer)

    # Last moves
    last_moved_time = pygame.time.get_ticks()
    # Main Loop
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                input_handler.handle_event(event)

        screen.fill(BG_COLOR)
        clock.tick(FPS)

        # Render Everything else:
        renderer = Renderer(screen, food, snake)
        renderer.add()
        renderer.draw()

        # Handle game states
        game_manager.check_collosion()
        game_manager.check_state()

        current_time = pygame.time.get_ticks()
        if current_time - last_moved_time >= RENDER_DELAY:
            snake.move()

            last_moved_time = current_time

        pygame.display.update()

    game_manager.print_score()

    pygame.quit()


if __name__ == "__main__":
    main()
