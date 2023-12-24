from .agent import Agent
import pandas as pd
import numpy as np

class PreferenceMatrix:
  def __init__(self, n_time_slot: int, agents : list[Agent]):
    if len(agents) != n_time_slot : raise ValueError("# of agents and # of time_slot are not same")
    self.n_time_slot = n_time_slot
    self.agents = agents
    self.rownames = [agent.name for agent in self.agents]
    self.colnames = [ f"t{j}" for j in range(0,self.n_time_slot)]
    self.dichotomous = self.gen_dichotomous_preference_matrix()
    self.ordered = self.gen_ordered_preference_matrix()
    self.zeros = pd.DataFrame(np.zeros_like(self.dichotomous), index=self.rownames, columns=self.colnames)
  
  def gen_matrix(self, pref_list):
    matrix = np.vstack(pref_list)
    return pd.DataFrame(matrix, index=self.rownames, columns=self.colnames)

  def gen_dichotomous_preference_matrix(self):
    d_pref_list = [agent.dichotomous_prefrence for agent in self.agents]
    return self.gen_matrix(d_pref_list)
  
  def gen_ordered_preference_matrix(self):
    o_pref_list = [agent.ordered_preference for agent in self.agents]
    return self.gen_matrix(o_pref_list)