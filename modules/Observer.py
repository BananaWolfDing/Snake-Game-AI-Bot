from configs import configs

stdMove = [[0, -1], [1, 0], [0, 1], [-1, 0]]

class Observer:
    def __init__(self, snake, food, width = configs.WIDTH, height = configs.HEIGHT):
        self.snake = snake
        self.food = food
        self.width = width
        self.height = height

    def towardsFood(self):
        x, y = self.foodDist()
        return y > 0

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
        l = (self.snake.getDirection() + 3) % 4
        f = self.snake.getDirection()
        r = (self.snake.getDirection() + 1) % 4
        return self.__explorer(l), self.__explorer(f), self.__explorer(r)

    def __explorer(self, dirction):
        x, y = self.snake.getHead()
        step = 1
        while (self.snake.legal(x + stdMove[dirction][0], y + stdMove[dirction][1])):
            x += stdMove[dirction][0]
            y += stdMove[dirction][1]
            step += 1

        return step

    def observe(self):
        return [self.foodDist(), self.wallDist(), self.selfDist()]
