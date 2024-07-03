# train_dqn.py
import gym
import numpy as np

def train_dqn(env_name):
    env = gym.make(env_name)
    state = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        next_state, reward, done, _ = env.step(action)
        state = next_state

# 主程式
if __name__ == "__main__":
    env_name = 'CartPole-v1'
    train_dqn(env_name)