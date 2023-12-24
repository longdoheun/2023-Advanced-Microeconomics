import numpy as np
import random

class Agent:
  def __init__(self, name, n_time_slot):
    self.name = name
    self.n_time_slot = n_time_slot
    self.ordered_preference = self.gen_ordered_preference()
    self.dichotomous_prefrence = self.gen_dichotomous_prefernence()

  def gen_ordered_preference(self):
    n_available_time = random.randint(2, self.n_time_slot)
    preference = np.concatenate((np.arange(1, n_available_time+1), np.zeros(self.n_time_slot-n_available_time, dtype=int)))
    np.random.shuffle(preference)
    return preference
  
  def gen_dichotomous_prefernence(self):
    dichotomous_prefernence = self.ordered_preference.copy()
    dichotomous_prefernence[dichotomous_prefernence != 0] = 1
    return dichotomous_prefernence