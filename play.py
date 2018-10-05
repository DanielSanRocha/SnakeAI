import pygame
from objects.level import Level
from config import SCREEN_WIDTH,SCREEN_HEIGHT,GRID_SIZE_X,GRID_SIZE_Y,BACKGROUND_COLOR

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
        clock.tick(4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys=pygame.key.get_pressed()

        control = level.snake.getDirection()
        if keys[pygame.K_UP]:
            control = 0
        elif keys[pygame.K_RIGHT]:
            control = 1
        elif keys[pygame.K_DOWN]:
            control = 2
        elif keys[pygame.K_LEFT]:
            control = 3


        screen.fill(BACKGROUND_COLOR)
        level.tick(screen, deltaTime, control)
        pygame.display.flip()

    pygame.quit()

if __name__=="__main__":
    main()
