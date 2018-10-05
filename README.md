# SnakeAI
Snake Game with reinforcement Q-learning and neural networks!

### Description
 A simple python program using keras to train a neural network to play the snake game.

### Installing
 First ensure you have pygame, keras and tensorflow (or other backend that you like =)) to run the program. I recommend using conda virtual environments.

### Commands
To play the game controlling the snake with the arrow keys run
 ```console
 python play.py
 ```
 For train/watch the neural network, run
 ```console
 python ai_play.py
 ```
### Configuration Parameters
In config.py you will encounter several parameters that can be adjusted as you like. A quick summary of each of the parameters:

#### Game Parameters

##### SCREEN_WIDTH:
Determine the width of the screen in pixels. Has not to do with the grid_size. Always ensure that this number is divisible by GRID_SIZE_X.

##### SCREEN_HEIGHT:
Determine the height of the screen in pixels. Has not to do with the grid size. Always ensure that this number is divisible by GRID_SIZE_Y.

##### GRID_SIZE_X:
The amount of squares in the grid on the horizontal component.

##### GRID_SIZE_Y:
The amount of squares in the grid on the vertical component.

##### BACKGROUND_COLOR:
The color of the background in RGB.

##### FRAME_RATE:
The framerate that the game will run. Also determine the velocity of the training. FRAME_RATE = 0 will let your computer run as fast as possible. A good frame rate to watch is 15.

#### DQN Parameters

##### GAMMA:
The learning rate for the q-function.

##### EXPLORATION_COEFFICIENT:
The probability of the snake do a random decision (for training purpose).

##### EXPLORATION_COEFFICIENT_DECAY:
After each training, the EXPLORATION_COEFFICIENT will decay by this amount until it is zero (this value can be zero).

##### LEARNING_RATE:
The learning rate of the 'Adam' algorithm of the neural network.

##### EPOCHS:
How many times the neural network should be trained against each memories.

##### TRAIN_INTERVAL:
How many memories should be collected before each training. For example, with 1, the neural network is trained each frame. Put 0 for no training.

#### Reward Parameters

#####DEATH_REWARD:
Reward after death.

##### EAT_FRUIT_REWARD:
Reward after the snake is able to eat a fruit.

##### FOOD_DISTANCE_REWARD_MULTIPLICATION_FACTOR, FOOD_DISTANCE_REWARD_LINEAR_FACTOR:
The snake receive a reward depending on it distance from the fruit given by the formula reward = FOOD_DISTANCE_REWARD_MULTIPLICATION_FACTOR/distance + FOOD_DISTANCE_REWARD_LINEAR_FACTOR.

# FileIO Parameters

##### BRAIN_LOAD_FILENAME:
The weights of the neural network will be loaded from the filename in this parameter. You can leave it empty for a empty neural network.

##### BRAIN_SAVE_FILENAME:
The weights of the neural network will be saved with this filename in this parameter. You can leave it empty for not saving.
