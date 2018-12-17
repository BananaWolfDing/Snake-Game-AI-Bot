import pygame
import sys
from configs import configs
from modules.Game import Game
from train.Experience import ERM
from train.NeuralNetwork import NeuralNetwork
erm = ERM()
erm.loadData()

pygame.init()
screen = pygame.display.set_mode((configs.WIN_WIDTH, configs.WIN_HEIGHT))
pygame.display.set_caption("Snake Game AI Bot")

game = Game(screen)
nn = NeuralNetwork()
nn.loadModel()

dirc = 0
while True:
    observe, reward, len, lose = game.moveByRelativeDirection(dirc)
    if not lose:
        dirc = nn.predict(observe)

    pygame.display.update()
    pygame.time.Clock().tick(configs.GAME_FPS)