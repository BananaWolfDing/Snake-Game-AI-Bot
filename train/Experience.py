import random
import pickle
from configs import LearningConfigs
from modules.Game import Game

class ERM:
    def saveData(self, data, path = LearningConfigs.DATA_PATH):
        with open(path, 'wb') as output:
            pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)

    def loadData(self, path = LearningConfigs.DATA_PATH):
        with open(path, 'rb') as input:
            return pickle.load(input)

    def generateTrainingData(self, size = LearningConfigs.SAMPLE_SIZE, aim = LearningConfigs.AIM_SCORE):
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
                    cache.append([observer, self.oneHotMove(movement)])
                    score += reward
                else:
                    break

            if (score >= aim):
                data.append([cache, score])
                dataSize += 1
                print("Training data({:d}/{:d}): Score = {:d}".format(len(data), size, score))

        print("Training data ready!")
        return data

    def oneHotMove(self, x):
        if x == -1:
            return [1, 0, 0]
        elif x == 0:
            return [0, 1, 0]
        elif x == 1:
            return [0, 0, 1]

if __name__ == "__main__":
    erm = ERM()
    data = erm.generateTrainingData()
    erm.saveData(data)
