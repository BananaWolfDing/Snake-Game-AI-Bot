import pygame
from modules.Game import Game
from train.NeuralNetwork import NeuralNetwork
from train.Experience import ERM


def test(nn):
    game = Game()

    dirc = 0
    while True:
        observe, reward, length, lose = game.moveByRelativeDirection(dirc)
        if not lose:
            dirc = nn.predict(observe)
        else:
            return length


nn = NeuralNetwork()
erm = ERM()

data = erm.loadData()

nn.train(data)
nn.saveModel()

print("Score = " + str(test(nn)))
