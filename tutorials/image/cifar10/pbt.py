"""Population-based Training

exploit() - Calculate CIFAR Inception score

explore() - Perform cross-over and mutation

"""
import random
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
  
def exploit(losses, hyperparams):
  print ('Ready, do Exploit')
  # Replace the last FLAGS.pbt_truncate_percentage of tower hyperparam with
  # the first FLAGS.pbt_truncate_percentage of tower hyperparam

  print ('Replace %d tower' % REPLACE_TOWER)
  
  print ('old hyperparameters')
  for item in hyperparams:
    print item
  print '\n'

  print ('Loss of each tower')
  print (losses)
  
  bad_indices = sorted(range(POPULATION), key=lambda i: losses[i])[-REPLACE_TOWER:]
  good_indices = sorted(range(POPULATION), key=lambda i: losses[i])[:REPLACE_TOWER]

  print (bad_indices)
  print (good_indices)

  for i in xrange(REPLACE_TOWER):
    hyperparams[bad_indices[i]] = hyperparams[good_indices[i]]

  print ('new hyperparameters')
  for item in hyperparams:
    print item
  print '\n'

  return hyperparams

def explore(learning_rates, batch_sizes):
  #do crossover
  
  #do mutation
  return learning_rates, batch_sizes

def random_init_lr():
  return random.uniform(INITIAL_LEARNING_RATE_LOWER_BOUND,
                        INITIAL_LEARNING_RATE_UPPER_BOUND)
