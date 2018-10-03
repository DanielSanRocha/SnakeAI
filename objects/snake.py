import pygame

GREEN = (0,255,0)
# 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT

class Snake:
    def __init__(self,x,y,pixel_size_x,pixel_size_y):
        self.x = x
        self.y = y
        self.pixel_size_x = pixel_size_x
        self.pixel_size_y = pixel_size_y
        self.direction = 0

        self.pieces = [[x,y]]
        self.lastPieceLastPosition = [x,y]

    def tick(self,screen,deltaTime,control):
        self.lastPieceLastPosition = self.pieces[len(self.pieces)-1]
        self.move(control)
        for piece in self.pieces:
            pygame.draw.rect(screen, GREEN, pygame.Rect(
            piece[0]*self.pixel_size_x, piece[1]*self.pixel_size_y,
            self.pixel_size_x,self.pixel_size_y))

    def move(self,control):
        if control != -1:
            if self.direction - control != 2 and self.direction - control != -2:
                self.direction = control

        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1

        for i in reversed(range(1,len(self.pieces))):
            self.pieces[i] = self.pieces[i-1]

        self.pieces[0] = [self.x,self.y]

    def hasTouchedItself(self):
        for i in range(1,len(self.pieces)):
            if self.pieces[i][0] == self.x and self.pieces[i][1] == self.y:
                return True
        return False

    def grow(self):
        new_piece = self.lastPieceLastPosition
        self.pieces.append(new_piece)
