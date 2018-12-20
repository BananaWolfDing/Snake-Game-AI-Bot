from configs import LearningConfigs
from modules.Snake import Snake
from modules.Food import Food
from modules.Render import Render
from modules.Observer import Observer

class Game:
    def __init__(self, screen = None):
        self.screen = screen
        self.snake = Snake()
        self.food = Food(self.snake)
        self.render = Render(screen)
        self.render.background()
        x, y = self.food.getFood()
        self.render.food(x, y)
        x, y = self.snake.getHead()
        self.render.snakeHead(x, y)
        self.observer = Observer(self.snake, self.food)

    def moveByRelativeDirection(self, direction):
        absDirc = (self.snake.getDirection() + direction + 4) % 4
        return self.moveByAbsoluteDirection(absDirc)

    def moveByAbsoluteDirection(self, direction):
        if (direction - self.snake.getDirection() + 4) % 4 == 2:
            direction = (direction + 4) % 2
        self.snake.changeDirection(direction)

        reward = LearningConfigs.ALIVE
        if self.observer.towardsFood():
            reward += LearningConfigs.TO_FOOD

        x, y = self.snake.nextStepPos()
        if (x == self.food.x) and (y == self.food.y):
            x, y = self.snake.getHead()
            self.render.snakeBody(x, y)

            res = self.snake.extend()

            x, y = self.snake.getHead()
            self.render.snakeHead(x, y)
            self.food.randFood(self.snake)
            x, y = self.food.getFood()
            self.render.food(x, y)
            reward += LearningConfigs.EAT_FOOD
        else:
            x, y = self.snake.getHead()
            s, t = self.snake.getTail()
            self.render.snakeBody(x, y)

            res = self.snake.move()
            if res:
                x, y = self.snake.getHead()
                self.render.snakeHead(x, y)
                self.render.null(s, t)

        if res:
            observe = self.observer.observe()
            return observe, reward, self.snake.length(), False
        else:
            return None, None, self.snake.length() + 1, True
