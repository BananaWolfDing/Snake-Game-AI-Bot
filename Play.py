import pygame
import sys
import configs
from Game import Game

pygame.init()
screen = pygame.display.set_mode(configs.WIN_WIDTH, configs.WIN_HEIGHT)
pygame.display.set_caption("Ding Snake Game")

game = Game(screen)

while True:
    event = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                direction = 0
            elif event.key == K_RIGHT:
                direction = 1
            elif event.key == K_DOWN:
                direction = 2
            elif event.key == K_LEFT:
                direction = 3

            observe, reward, len, lose = Game.moveByAbsoluteDirection(direction)
            if lose:
                sys.exit()

    if event == None:
        observe, reward, len, lose = Game.moveByRelativeDirection(0)
        if lose:
            sys.exit()

    pygame.display.update()
    pygame.time.Clock().tick(configs.GAME_FPS)
