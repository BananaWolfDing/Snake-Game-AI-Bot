from Snake import Snake
from Food import Food
from Render import Render

class Game:
    def __init__(self, screen = None):
        self.screen = screen
        self.snake = Snake()
        self.food = Food(self.snake)
        self.render = Render(screen)
        Render.background()
        x, y = Food.getFood()
        Render.food(x, y)
        x, y = Snake.getHead()
        Render.snakeHead(x, y)

    def moveByRelativeDirection(self, direction):
        absDirc = (self.snake.getDirection() + direction + 4) % 4
        self.moveByAbsoluteDirection(absDirc)

    def moveByAbsoluteDirection(self, direction):
        if (direction - self.snake.getDirection() + 4) % 4 == 2:
            direction = (direction + 4) % 2
        self.snake.changeDirection(direction)

        x, y = self.snake.nextStepPos()
        if (x == self.food.x) and (y == self.food.y):
            x, y = self.snake.getHead()
            Render.snakeBody(x, y)

            res = self.snake.extend()

            x, y = self.snake.getHead()
            Render.snakeHead(x, y)
            self.food.randFood(self.snake)
        else:
            x, y = self.snake.getHead()
            s, t = self.snake.getTail()
            Render.snakeBody(x, y)

            res = self.snake.move()
            x, y = self.snake.getHead()
            Render.snakeHead(x, y)
            Render.null(s, t)

        observe = None
        reward = None
        return observe, reward, len, res