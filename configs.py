# Game Speed Settings
GAME_FPS = 1

# Grid Settings
WIDTH = 20
HEIGHT = 20

# Game Configs
DIRECTION = 0
START_BODY = [{
    'x': WIDTH / 2,
    'y': HEIGHT / 2
}]

# Display Settings
PIXEL_SIZE = 20
BOUND_SIZE = 3
WIN_WIDTH = WIDTH * PIXEL_SIZE + BOUND_SIZE * 2
WIN_HEIGHT = HEIGHT * PIXEL_SIZE + BOUND_SIZE * 2

# Color Settings
GRID_COLOR = (255, 255, 255) # White
SNAKE_COLOR = (255, 0, 0) # Red
BODY_COLOR = (0, 0, 255) # Blue
FOOD_COLOR = (0, 0, 0) # Black
BOUND_COLOR = (180, 180, 180) # Gray