import pygame
from modules.Game import Game
from train.NeuralNetwork import NeuralNetwork
from train.Experience import ERM


def test(nn):
    game = Game()

    dirc = 0
    score = 0
    while True:
        observe, reward, len, lose = game.moveByRelativeDirection(dirc)
        if not lose:
            dirc = nn.predict(observe)
        else:
            return len


nn = NeuralNetwork()
erm = ERM()

data = erm.loadData()

nn.train(data)
nn.saveModel()

print("Score = " + str(test(nn)))
