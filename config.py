# Game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE_X = 6
GRID_SIZE_Y = 6
BACKGROUND_COLOR = (0,0,0)
FRAME_RATE = 15 # 0 for as fast as possible

# DQN Parameters
GAMMA = 0.2
EXPLORATION_COEFFICIENT = 0.05
EXPLORATION_COEFFICIENT_DECAY = 0.00
LEARNING_RATE = 0.004
EPOCHS = 1
TRAIN_INTERVAL = 50

# Reward Parameters
DEATH_REWARD = -5
EAT_FRUIT_REWARD = 5
FOOD_DISTANCE_REWARD_MULTIPLICATION_FACTOR = 1
FOOD_DISTANCE_REWARD_LINEAR_FACTOR = 1

# FileIO Parameters
BRAIN_LOAD_FILENAME = "brain.h5" #Leave a empty for not loading a brain
BRAIN_SAVE_FILENAME = "brain.h5" #Leave a empty for not saving the brain
