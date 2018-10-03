import random

from food import Food
from snake import Snake

class Level:
    def __init__(self,grid_size_x, grid_size_y,screen_size_x,screen_size_y):
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.screen_size_x = screen_size_x
        self.screen_size_y = screen_size_y

        self.block_size_x = self.screen_size_x/self.grid_size_x
        self.block_size_y = self.screen_size_y/self.grid_size_y

        self.snake = Snake(self.grid_size_x/2,self.grid_size_y/2,self.block_size_x,self.block_size_y)
        self.spawnFood()

    def tick(self,screen,delta,control):
        self.snake.tick(screen,delta,control)
        self.food.tick(screen,delta)

        if self.snakeOutOfBounds() or self.snake.hasTouchedItself():
            self.reset()

        if self.snakeHasTouchedFood():
            self.snake.grow()
            self.spawnFood()

    def snakeHasTouchedFood(self):
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            return True
        else:
            return False

    def spawnFood(self):
        x = random.randint(0,self.grid_size_x-1)
        y = random.randint(0,self.grid_size_y-1)
        food = Food(x,y,self.block_size_x,self.block_size_y)
        self.food = food

    def snakeOutOfBounds(self):
        if self.snake.x > self.grid_size_x or self.snake.y > self.grid_size_y or self.snake.x < 0 or self.snake.y < 0:
            return True
        else:
            return False

    def reset(self):
        self.foods = []
        self.spawnCount = 0
        self.snake = Snake(self.grid_size_x/2,self.grid_size_y/2,self.block_size_x,self.block_size_y)
