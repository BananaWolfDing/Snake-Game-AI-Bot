import configs

stdMove = [[0, -1], [1, 0], [0, 1], [-1, 0]]

class Snake:
    def __init__(self):
        self.gridWidth = configs.WIDTH
        self.gridHeight = configs.HEIGHT
        self.dirc = configs.DIRECTION
        self.win = None
        self.body = configs.START_BODY

    def length(self):
        return len(self.body)

    def getDirection(self):
        return self.dirc

    def getHead(self):
        return self.body[0]['x'], self.body[0]['y']

    def getTail(self):
        return self.body[-1]['x'], self.body[-1]['y']

    def nextStepPos(self):
        x = self.body[0]['x'] + stdMove[self.dirc][0]
        y = self.body[0]['y'] + stdMove[self.dirc][1]
        return x, y

    def changeDirection(self, direction):
        if (self.dirc - direction + 4) % 4 == 2:
            return
        else:
            self.dirc = direction

    def won(self):
        return self.length() >= self.gridWidth * self.gridHeight

    def move(self):
        x, y = self.nextStepPos()
        del self.body[-1]

        if self.legal(x, y):
            self.body.insert(0, {'x': x, 'y': y})
            return True
        else:
            return False

    def extend(self):
        x, y = self.nextStepPos()

        if self.legal(x, y):
            self.body.insert(0, {'x': x, 'y': y})
            if self.length() == self.gridWidth * self.gridHeight:
                self.win = True
            return True
        else:
            return False

    def partOfBody(self, x, y):
        for component in self.body:
            if component['x'] == x and component['y'] == y:
                return True

        return False

    def legal(self, x, y):
        if x < 0 or y < 0 or x >= self.gridWidth or y >= self.gridHeight:
            return False

        if self.partOfBody(x, y):
            return False

        return True
