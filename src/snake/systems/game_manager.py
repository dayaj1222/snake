import pygame
from pygame import Vector2

from snake.config import GRID_DIM, HEIGHT, RENDER_DELAY, RIGHT, WIDTH, GameState
from snake.entities.food import Food
from snake.entities.player import Snake
from snake.systems.input import InputHandler
from snake.systems.renderer import Renderer
from snake.windows import game_over_screen


class GameManager:
    def __init__(
        self,
        screen: pygame.surface.Surface,
        clock: pygame.time.Clock,
        snake: Snake,
        food: Food,
        renderer: Renderer,
        input_handler: InputHandler,
        game_over_screen: game_over_screen.GameOverScreen,
    ):
        self.screen = screen
        self.clock = clock
        self.snake = snake
        self.food = food
        self.renderer = renderer
        self.state: GameState = GameState.PLAYING
        self.score: int = 0
        self.input_handler = input_handler
        self.game_over_screen = game_over_screen

        # Internal
        self.last_moved_time = pygame.time.get_ticks()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = GameState.EXIT

            if self.state == GameState.PLAYING and event.type == pygame.KEYDOWN:
                self.input_handler.handle_event(event)

            if (
                self.state == GameState.GAME_OVER
                and event.type == pygame.MOUSEBUTTONDOWN
            ):
                new_state = self.game_over_screen.handle_click(event.pos)
                if new_state == GameState.PLAYING:
                    self.restart_game()
                elif new_state == GameState.EXIT:
                    self.state = GameState.EXIT

    def check_collision(self):
        # Wall collision
        if (
            self.snake.head.pos.x < 0
            or self.snake.head.pos.x >= WIDTH
            or self.snake.head.pos.y < 0
            or self.snake.head.pos.y >= HEIGHT
        ):
            self.state = GameState.GAME_OVER

        # Food collision
        if self.snake.head.pos == self.food.pos:
            self.score += 1
            self.food.update()
            self.snake.grow()

        # Self collision
        for piece in self.snake.pieces[1:]:
            if self.snake.head.pos == piece.pos:
                self.state = GameState.GAME_OVER

    def render(self):
        self.renderer.clear()
        self.renderer.draw(GameState.PLAYING, self.score)
        if self.state == GameState.GAME_OVER:
            self.game_over_screen.draw(self.score)
        self.renderer.update()

    def update(self):
        self.clock.tick()
        current_time = pygame.time.get_ticks()
        if current_time - self.last_moved_time >= RENDER_DELAY:
            self.snake.move()
            self.last_moved_time = current_time

    def restart_game(self):
        # Reset snake
        self.snake.head.pos = Vector2(GRID_DIM * 2, 0)
        self.snake.head.direction = RIGHT
        self.snake.pieces = [self.snake.head, self.snake.body]
        self.snake.body.pos = Vector2(0, 0)

        # Reset food
        self.food.update()

        # Reset score and state
        self.score = 0
        self.state = GameState.PLAYING
