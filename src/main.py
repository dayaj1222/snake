import pygame
from pygame import Vector2

from snake.config import FOOD_POSITION, HEIGHT, WIDTH, GameState
from snake.entities.food import Food
from snake.entities.player import Block, Head, Snake
from snake.systems.game_manager import GameManager
from snake.systems.input import InputHandler
from snake.systems.renderer import Renderer
from snake.widgets.score import Score
from snake.windows.game_over_screen import GameOverScreen


def main():
    # Initialize pygame
    pygame.init()

    # Create main Window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    # Pygame Clock
    clock = pygame.time.Clock()

    # Score widget
    score = Score()

    # Initialize Game Objects
    food = Food(pos=Vector2(FOOD_POSITION))
    head = Head()
    body = Block()
    snake = Snake(
        head,
        body,
    )

    # Initialize game over screen
    game_over_screen = GameOverScreen(screen)

    # Initialize Input Handler
    input_handler = InputHandler(snake)

    # Initialize Renderer
    renderer = Renderer(screen, food, snake, score)

    # Initialize GameManager
    game_manager = GameManager(
        screen=screen,
        clock=clock,
        snake=snake,
        food=food,
        renderer=renderer,
        input_handler=input_handler,
        game_over_screen=game_over_screen,
    )

    # Main Loop
    running = True
    while running:
        game_manager.process_events()

        if game_manager.state == GameState.PLAYING:
            game_manager.check_collision()
            game_manager.update()
        elif game_manager.state == GameState.GAME_OVER:
            pass
        elif game_manager.state == GameState.EXIT:
            running = False

        game_manager.render()

    pygame.quit()


if __name__ == "__main__":
    main()
