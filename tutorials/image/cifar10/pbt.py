"""Population-based Training

# Exploit - Calculate CIFAR Inception score

# Explore - Perform cross-over and mutation

"""
import random

INITIAL_LEARNING_RATE_UPPER_BOUND = 0.2
INITIAL_LEARNING_RATE_LOWER_BOUND = 0.01

def exploit():
  return 'Ready, do Exploit'

def explore(cross_over, mutation):
  #if cross_over:
    #do crossover
  #if mutation:
    #do mutation
  return 'Do explore'

def random_init_lr():
  return random.uniform(INITIAL_LEARNING_RATE_LOWER_BOUND,
                        INITIAL_LEARNING_RATE_UPPER_BOUND)