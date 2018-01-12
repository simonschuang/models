"""Population-based Training

exploit() - Calculate CIFAR Inception score

explore() - Perform cross-over and mutation

"""
import random
import numpy as np
import tensorflow as tf
from six.moves import xrange

INITIAL_LEARNING_RATE_UPPER_BOUND = 0.2
INITIAL_LEARNING_RATE_LOWER_BOUND = 0.01

# num of tower = num of GPUs, calculate num of tower to be replaced
REPLACE_TOWER = 0
POPULATION = 0
sess = None

class hyperparam:
  def __init(self):
    self.learning_rate = 0
    self.batch_size = 0

def setup(session, population, truncate_percentage):
  global POPULATION
  global REPLACE_TOWER
  global sess
  sess = session
  POPULATION = population
  REPLACE_TOWER = (population * truncate_percentage + 100) / 100
  print ('Setup replace %d of tower hyperparam' % REPLACE_TOWER)
  
def exploit(losses, hyperparams, changed_hp):
  print ('Ready, do Exploit')
  # Replace the last FLAGS.pbt_truncate_percentage of tower hyperparam with
  # the first FLAGS.pbt_truncate_percentage of tower hyperparam

  print ('Replace %d tower' % REPLACE_TOWER)
  
#  print ('old hyperparameters')
#  for item in hyperparams:
#    print item
#  print '\n'

#  print ('Loss of each tower')
#  print (losses)
  
  bad_indices = sorted(range(POPULATION), key=lambda i: losses[i])[-REPLACE_TOWER:]
  good_indices = sorted(range(POPULATION), key=lambda i: losses[i])[:REPLACE_TOWER]

#  print ('bad losses: %s' % (bad_indices))
#  print ('good losses: %s' % (good_indices))

  for i in xrange(REPLACE_TOWER):
    if hyperparams[bad_indices[i]] != hyperparams[good_indices[i]]:
      hyperparams[bad_indices[i]] = hyperparams[good_indices[i]]
      changed_hp[bad_indices[i]]=True

#  print ('new hyperparameters')
#  for item in hyperparams:
#    print item
#  print '\n'

  return hyperparams

def explore(hyperparams, changed_hp, shift_right=True, hptype=None):
#  print ('old hyperparameters')
#  for item in hyperparams:
#    print item
#  print '\n'
  #do crossover
#  if (shift_right):
#    hyperparams.insert(0,hyperparams.pop(-1))
#  else:
#    hyperparams.append(hyperparams.pop(0))
  #do mutation
  for idx, item in enumerate(hyperparams):
   if (changed_hp[idx]):
     if (hptype=='learning_rate'):
       lr=np.multiply(sess.run(item), random.choice([0.8,1.2]), dtype=np.float32)
       hyperparams[idx] = lr
     elif (hptype=='batch_size'):
       hyperparams[idx] = (hyperparams[idx] + random.choice([-1, 1])) % POPULATION

#  print ('new hyperparameters')
#  for item in hyperparams:
#    print item
#  print '\n'
  return hyperparams 

def random_init_lr():
  return random.uniform(INITIAL_LEARNING_RATE_LOWER_BOUND,
                        INITIAL_LEARNING_RATE_UPPER_BOUND)
