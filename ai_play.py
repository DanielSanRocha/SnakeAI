import pygame
from objects.level import Level
from agent import Agent

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE_X = 6
GRID_SIZE_Y = 6
BLACK = (0,0,0)
TRAIN_INTERVAL = 50

def main():
    pygame.init()
    pygame.display.set_caption("SnakeAI")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    running = True

    level = Level(GRID_SIZE_X,GRID_SIZE_Y,SCREEN_WIDTH,SCREEN_HEIGHT)
    getTicksLastFrame = 0

    agent = Agent(GRID_SIZE_X,GRID_SIZE_Y,4)
    agent.loadNeuralNetwork()
    train_counter = 0

    while running:
        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys=pygame.key.get_pressed()

        state = level.getState()
        control = agent.predict(state)

        screen.fill(BLACK)
        state = level.getState()
        result = level.tick(screen, deltaTime, control)
        next_state = level.getState()
        distance = level.getFoodSnakeDistance()
        agent.remember(state, control, next_state, distance, result)
        pygame.display.flip()

        train_counter += 1
        if train_counter == TRAIN_INTERVAL:
            train_counter = 0
            agent.train()

    agent.saveNeuralNetwork()
    # agent.saveMemories()
    pygame.quit()

if __name__=="__main__":
    main()
