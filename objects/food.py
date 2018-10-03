import pygame

BLUE = (0,0,255)

class Food:
    def __init__(self,x,y,pixel_size_x,pixel_size_y):
        self.x = x
        self.y = y
        self.pixel_size_x = pixel_size_x
        self.pixel_size_y = pixel_size_y

    def tick(self,screen,deltaTime):
        pygame.draw.rect(screen, BLUE, pygame.Rect(self.x*self.pixel_size_x, self.y*self.pixel_size_y, self.pixel_size_x,self.pixel_size_y))
