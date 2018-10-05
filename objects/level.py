import random,math
import numpy as np

from objects.food import Food
from objects.snake import Snake


class Level:
    def __init__(self,grid_size_x, grid_size_y,screen_size_x,screen_size_y):
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.screen_size_x = screen_size_x
        self.screen_size_y = screen_size_y

        self.block_size_x = self.screen_size_x/self.grid_size_x
        self.block_size_y = self.screen_size_y/self.grid_size_y

        self.snake = Snake(round(self.grid_size_x/2),round(self.grid_size_y/2),self.block_size_x,self.block_size_y)
        self.spawnFood()

    def tick(self,screen,delta,control):
        self.snake.tick(screen,delta,control)
        self.food.tick(screen,delta)

        if self.snakeHasTouchedFood():
            self.snake.grow()
            self.spawnFood()
            return 1

        if self.snakeOutOfBounds() or self.snake.hasTouchedItself():
            self.reset()
            return -1

        return 0

    def snakeHasTouchedFood(self):
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            return True
        else:
            return False

    def spawnFood(self):
        if len(self.snake.pieces) == self.grid_size_x * self.grid_size_y:
            self.reset()
            return

        x = random.randint(0,self.grid_size_x-1)
        y = random.randint(0,self.grid_size_y-1)
        if self.snake.contains(x,y):
            self.spawnFood()
            return

        food = Food(x,y,self.block_size_x,self.block_size_y)
        self.food = food

    def snakeOutOfBounds(self):
        if self.snake.x >= self.grid_size_x or self.snake.y >= self.grid_size_y or self.snake.x < 0 or self.snake.y < 0:
            return True
        else:
            return False

    def reset(self):
        self.foods = []
        self.spawnCount = 0
        self.snake = Snake(round(self.grid_size_x/2),round(self.grid_size_y/2),self.block_size_x,self.block_size_y)

    def getState(self):
        state = np.zeros((3, self.grid_size_x,self.grid_size_y))

        state[0,self.snake.x,self.snake.y] = 1

        pieces = self.snake.getPieces()
        for index in range(1,len(pieces)):
            piece = pieces[index]
            state[1,piece[0], piece[1]] = 1

        state[2, self.food.x, self.food.y] = 1

        return state.tolist()

    def getFoodSnakeDistance(self):
        return math.sqrt((self.snake.x - self.food.x)**2 + (self.snake.y - self.food.y)**2)
