import pygame
from configs import configs


class Render:
    def __init__(self, screen = None):
        self.screen = screen
        self.pixelSize = configs.PIXEL_SIZE
        self.boundSize = configs.BOUND_SIZE
        self.winWidth = configs.WIN_HEIGHT
        self.winHeight = configs.WIN_HEIGHT
        self.width = configs.WIDTH
        self.height = configs.HEIGHT

    def background(self):
        if self.screen is None:
            return
        boundRect = pygame.Rect(0, 0, self.winWidth, self.winHeight)
        pygame.draw.rect(self.screen, configs.BOUND_COLOR, boundRect)

        gridRect = pygame.Rect(self.boundSize, self.boundSize, self.width * self.pixelSize, self.height * self.pixelSize)
        pygame.draw.rect(self.screen, configs.GRID_COLOR, gridRect)

    def food(self, x, y):
        self.grid(x, y, configs.FOOD_COLOR)

    def snakeBody(self, x, y):
        self.grid(x, y, configs.BODY_COLOR)

    def snakeHead(self, x, y):
        self.grid(x, y, configs.SNAKE_COLOR)

    def null(self, x, y):
        self.grid(x, y, configs.GRID_COLOR)

    def grid(self, x, y, color):
        if self.screen is None or not self.legal(x, y):
            return

        area = pygame.Rect(self.pixelSize * x + self.boundSize, self.pixelSize * y + self.boundSize, self.pixelSize, self.pixelSize)
        pygame.draw.rect(self.screen, color, area)

    def legal(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
