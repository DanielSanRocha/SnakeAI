import pygame
from objects.level import Level

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE_X = 20
GRID_SIZE_Y = 20
BLACK = (0,0,0)

def main():
    pygame.init()
    pygame.display.set_caption("SnakeAI")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    running = True

    level = Level(GRID_SIZE_X,GRID_SIZE_Y,SCREEN_WIDTH,SCREEN_HEIGHT)

    getTicksLastFrame = 0

    while running:
        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys=pygame.key.get_pressed()

        control = -1
        if keys[pygame.K_UP]:
            control = 0
        elif keys[pygame.K_RIGHT]:
            control = 1
        elif keys[pygame.K_DOWN]:
            control = 2
        elif keys[pygame.K_LEFT]:
            control = 3


        screen.fill(BLACK)

        level.tick(screen, deltaTime, control)

        pygame.display.flip()

    pygame.quit()

if __name__=="__main__":
    main()
