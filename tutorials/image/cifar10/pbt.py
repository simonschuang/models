"""Population-based Training

exploit() - Calculate CIFAR Inception score

explore() - Perform cross-over and mutation

"""
import random

INITIAL_LEARNING_RATE_UPPER_BOUND = 0.2
INITIAL_LEARNING_RATE_LOWER_BOUND = 0.01

def exploit():
  return 'Ready, do Exploit'

def explore(learning_rates, batch_sizes):
  #do crossover
  
  #do mutation
  return 'Do explore'

def random_init_lr():
  return random.uniform(INITIAL_LEARNING_RATE_LOWER_BOUND,
                        INITIAL_LEARNING_RATE_UPPER_BOUND)