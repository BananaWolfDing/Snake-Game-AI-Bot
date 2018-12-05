class Game:
    def move(self, direction):
        relativeDirection = self.__calcRelative(self.snake.getDirection(), direction)

    def __calcRelative(self, curDirc, aimDirc):
        r = (aimDirc - curDirc + 5) % 4 - 1
        if r == 2:
            return 0
        else:
            return r