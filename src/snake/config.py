from pathlib import Path

from pygame.math import Vector2

ROOT_DIR = Path(__file__).parent.parent
ASSET_DIR = ROOT_DIR / "assets"
IMAGE_DIR = ASSET_DIR / "images"

GRID_DIM = 32

HEIGHT = 800
WIDTH = 1200
BG_COLOR = 0x7DDA58
FPS = 60

# Directions
UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)
