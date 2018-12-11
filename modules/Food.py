import random
from configs import configs


class Food:
    def __init__(self, snake, width = configs.WIDTH, height = configs.HEIGHT, ):
        self.gridWidth = width
        self.gridHeight = height
        try:
            self.randFood(snake)
        except Exception as err:
            raise Exception(err)

    def randFood(self, snake):
        if snake.won():
            raise Exception("Grid is full")

        while True:
            x = random.randint(0, self.gridWidth - 1)
            y = random.randint(0, self.gridHeight - 1)
            if not snake.partOfBody(x, y):
                self.x = x
                self.y = y
                return

    def getFood(self):
        return self.x, self.y