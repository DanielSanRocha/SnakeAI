import random,json
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.optimizers import Adam
from keras.utils import to_categorical
import random

class Agent:
    def __init__(self, grid_size_x, grid_size_y, action_size):
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.action_size = action_size
        self.memories = {'state': [], 'next_state': [], 'action': [], 'distance': [], 'result': [], 'reward': []}

        self.epochs = 1
        self.learning_rate = 0.004
        self.stupidity_threshold = 0.001
        self.epsilon = 0.00
        self.delta_epsilon = 0.0001
        self.distance_food_reward_factor = 0.5
        self.gamma = 0.2

        self.model = self._build_model()

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
        reward = 0
        if result == -1:
            self.epsilon = 0
            reward = -5
        elif result == 0:
            self.epsilon += self.stupidity_threshold
            reward = self.distance_food_reward_factor/distance
        elif result == 1:
            self.epsilon = 0
            reward = 5

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

        if (act_values < self.stupidity_threshold).all():
            return random.randrange(self.action_size)

        return np.argmax(act_values[0])

    def train(self):
        if self.epsilon > 0:
            self.epsilon -= self.delta_epsilon
            print(self.epsilon)

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

    def saveMemories(self):
        with open('memories.json', 'w') as outfile:
            json.dump(self.memories, outfile)

    def saveNeuralNetwork(self):
        self.model.save_weights('brain.h5')

    def loadMemories(self):
        self.memories = np.load('memories.npy').tolist()

    def loadNeuralNetwork(self):
        self.model.load_weights('brain.h5')
