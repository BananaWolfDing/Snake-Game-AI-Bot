import LearningConfigs
import random
from Game import Game

def generateTrainingData(size = LearningConfigs.SAMPLE_SIZE, aim = LearningConfigs.AIM_SCORE):
    print("Begin generating training data...")

    data = []
    dataSize = 0

    while dataSize < size:
        game = Game()
        cache = []
        score = 0

        while True:
            movement = random.randint(-1, 1)
            observer, reward, len, lose = game.moveByRelativeDirection(movement)
            if not lose:
                cache.append([observer, oneHotMove(movement)])
                score += reward
            else:
                break

        if (score >= aim):
            data.append([cache, score])
            dataSize += 1
            print("Training data({:d}/{:d}): Score = {:d}".format(len(data), size, score))

    print("Training data ready!")

def oneHotMove(x):
    if x == -1:
        return [1, 0, 0]
    elif x == 0:
        return [0, 1, 0]
    elif x == 1:
        return [0, 0, 1]

if __name__ == "__main__":
    generateTrainingData()
