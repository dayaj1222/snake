import math
from enum import Enum, auto
from pathlib import Path

from pygame.math import Vector2

ROOT_DIR = Path(__file__).parent.parent
ASSET_DIR = ROOT_DIR / "assets"
IMAGE_DIR = ASSET_DIR / "images"

GRID_DIM = 20

# Dimentions
HEIGHT = 800
WIDTH = 1200

HEIGHT_BLOCKS = math.floor(HEIGHT / GRID_DIM)
WIDTH_BLOCKS = math.floor(WIDTH / GRID_DIM)

BG_COLOR = 0x7DDA58
FPS = 60
RENDER_DELAY = 300

# Directions
UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)


# States
class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()
