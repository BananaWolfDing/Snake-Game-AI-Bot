import pygame
import configs

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
        if (self.screen == None):
            return

        topRect = pygame.Rect(0, 0, self.width + self.boundSize * 2, self.boundSize)
        botRect = pygame.Rect(0, self.height + self.boundSize, self.width + 2 * self.boundSize, self.boundSize)
        lefRect = pygame.Rect(0, 0, self.boundSize, self.height + 2 * self.boundSize)
        rigRect = pygame.Rect(self.width + self.boundSize, 0, self.boundSize, self.height + 2 * self.boundSize)
        pygame.draw.rect(self.screen, configs.BOUND_COLOR, topRect)
        pygame.draw.rect(self.screen, configs.BOUND_COLOR, botRect)
        pygame.draw.rect(self.screen, configs.BOUND_COLOR, lefRect)
        pygame.draw.rect(self.screen, configs.BOUND_COLOR, rigRect)

        gridRect = pygame.Rect(self.boundSize, self.boundSize, self.width, self.height)
        pygame.draw.rect(self.screen, configs.GRID_COLOR, gridRect)

    def grid(self, x, y, color):
        if (self.screen == None):
            return

        area = pygame.Rect(self.pixelSize * x + self.boundSize, self.pixelSize * y, self.pixelSize, self.pixelSize)
        pygame.draw.rect(self.screen, area)