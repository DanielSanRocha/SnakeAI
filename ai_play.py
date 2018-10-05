import pygame
from objects.level import Level
from agent import Agent
from config import SCREEN_WIDTH,SCREEN_HEIGHT,GRID_SIZE_X,GRID_SIZE_Y,BACKGROUND_COLOR
from config import BRAIN_LOAD_FILENAME,BRAIN_SAVE_FILENAME,FRAME_RATE,TRAIN_INTERVAL

def main():
    pygame.init()
    pygame.display.set_caption("SnakeAI")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    running = True

    level = Level(GRID_SIZE_X,GRID_SIZE_Y,SCREEN_WIDTH,SCREEN_HEIGHT)

    agent = Agent(GRID_SIZE_X,GRID_SIZE_Y,4)
    if(BRAIN_LOAD_FILENAME):
        agent.loadNeuralNetwork(BRAIN_LOAD_FILENAME)
    train_counter = 0

    while running:
        deltaTime = clock.tick(FRAME_RATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys=pygame.key.get_pressed()

        state = level.getState()
        control = agent.predict(state)

        screen.fill(BACKGROUND_COLOR)
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

    if(BRAIN_SAVE_FILENAME):
        agent.saveNeuralNetwork(BRAIN_SAVE_FILENAME)
    pygame.quit()

if __name__=="__main__":
    main()
