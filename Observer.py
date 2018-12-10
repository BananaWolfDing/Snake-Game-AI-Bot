from Snake import Snake
import configs

class Observer:
    def __init__(self, snake, food, width = configs.WIDTH, height = configs.HEIGHT):
        self.snake = snake
        self.food = food
        self.width = width
        self.height = height

    def foodDist(self):
        dirc = self.snake.dirc
        x, y = self.snake.getHead()
        fx = self.food.x
        fy = self.food.y

        if dirc == 0:
            return fx - x, fy - y
        elif dirc == 1:
            return y - fy, fx - x
        elif dirc == 2:
            return x - fx, y - fy
        else:
            return fy - y, x - fx

    def wallDist(self):
        dirc = self.snake.dirc
        x, y = self.snake.getHead()
        w = self.width
        h = self.height

        if dirc == 0:
            return x, h - y, w - x
        elif dirc == 1:
            return h - y, w - x, y
        elif dirc == 2:
            return w - x, y, x
        else:
            return y, x, h - y

    def selfDist(self):
        return # To be finished