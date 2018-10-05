import random,json
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.optimizers import Adam
from keras.utils import to_categorical
import random

from config import LEARNING_RATE,EXPLORATION_COEFFICIENT,EXPLORATION_COEFFICIENT_DECAY,GAMMA,EPOCHS
from config import DEATH_REWARD,EAT_FRUIT_REWARD,FOOD_DISTANCE_REWARD_MULTIPLICATION_FACTOR,FOOD_DISTANCE_REWARD_LINEAR_FACTOR

class Agent:
    def __init__(self, grid_size_x, grid_size_y, action_size):
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.action_size = action_size
        self.memories = {'state': [], 'next_state': [], 'action': [], 'distance': [], 'result': [], 'reward': []}

        self.epochs = EPOCHS
        self.learning_rate = LEARNING_RATE
        self.epsilon = EXPLORATION_COEFFICIENT
        self.delta_epsilon = EXPLORATION_COEFFICIENT_DECAY
        self.food_distance_reward_linear_factor = FOOD_DISTANCE_REWARD_LINEAR_FACTOR
        self.food_distance_reward_multiplication_factor = FOOD_DISTANCE_REWARD_MULTIPLICATION_FACTOR
        self.gamma = GAMMA

        self.model = self._build_model()

    def calculateReward(self,distance,result):
        reward = 0
        if result == -1:
            reward = -5
        elif result == 0:
            reward = self.food_distance_reward_multiplication_factor/distance + self.food_distance_reward_linear_factor
        elif result == 1:
            reward = 5

        return reward

    def _build_model(self):
        model = Sequential()
        model.add(Dense(32, input_shape=(3,self.grid_size_x,self.grid_size_y), activation='relu'))
        model.add(Flatten())
        model.add(Dense(40, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, next_state, distance, result):
        reward = self.calculateReward(distance,result)

        self.memories['state'].append(state)
        self.memories['action'].append(action)
        self.memories['next_state'].append(next_state)
        self.memories['distance'].append(distance)
        self.memories['result'].append(result)
        self.memories['reward'].append(reward)

    def predict(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)

        act_values = self.model.predict(np.array([state]))
        return np.argmax(act_values[0])

    def train(self):
        if self.epsilon > 0:
            self.epsilon -= self.delta_epsilon

        X = np.array(self.memories['state'])
        Y = self.model.predict(X)
        Y_f = self.model.predict(np.array(self.memories['next_state']))

        for i in range(len(Y)):
            target = self.memories['reward'][i]
            if self.memories['result'][i] != -1:
                target = target + self.gamma * np.amax(Y_f[i])
            else:
                print(Y[i])

            Y[i][self.memories['action'][i]] = target

        self.model.fit(np.array(X),np.array(Y), epochs=self.epochs, verbose=0)

        self.memories = {'state': [], 'next_state': [], 'action': [], 'distance': [], 'result': [], 'reward': []}

    def saveNeuralNetwork(self,filename):
        self.model.save_weights(filename)

    def loadNeuralNetwork(self,filename):
        self.model.load_weights(filename)
