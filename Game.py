import Snake
import Food

class Game:
    def __init__(self, screen = None):
        self.screen = None
        self.snake = Snake()
        self.food = Food(self.snake)

    def moveByRelativeDirection(self, direction):
        return
    def moveByAbsoluteDirection(self, direction):
        relativeDirection = self.__calcRelative(self.snake.getDirection(), direction)
        self.moveByRelativeDirection(relativeDirection)

    def __calcRelative(self, curDirc, aimDirc):
        r = (aimDirc - curDirc + 5) % 4 - 1
        if r == 2:
            return 0
        else:
            return r