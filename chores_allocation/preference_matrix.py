"""
Module providing preference matrices
"""

import numpy as np
import pandas as pd
from .agent import Agent


class PreferenceMatrix:
    """Class to generate preference matrix.
        (i) dichotomous preference matrix
        (ii) ordered preference matrix

    Args:
        n_time_slot: the number of time slots; int
        agents: the list of class 'Agent'; list[Agent]

    Attributes:
        n_time_slot: the number of time slots; int
        agents: the list of class 'Agent'; list[Agent]
        rownames: the list of agents' name
        colnames: the list of time slots' name
        dichotomous : Datafroma of market capitalization data (panel)
        ordered : index of datetime
        zeros: dataframe filled with zeros, which is same size of the dichotomous
    """

    def __init__(self, n_time_slot: int, agents: list[Agent]):
        if len(agents) != n_time_slot:
            raise ValueError("# of agents and # of time slots are not same")
        self.n_time_slot = n_time_slot
        self.agents = agents
        self.rownames = [agent.name for agent in self.agents]
        self.colnames = [f"t{j}" for j in range(0, self.n_time_slot)]
        self.dichotomous = self.gen_dichotomous_preference_matrix()
        self.ordered = self.gen_ordered_preference_matrix()
        self.zeros = pd.DataFrame(
            np.zeros_like(self.dichotomous), index=self.rownames, columns=self.colnames
        )

    def gen_matrix(self, pref_list):
        """Generate matrix

        Args:
            pref_list:  row of each matrix; dataframe

        Returns:
            dataframe of matrix
        """
        matrix = np.vstack(pref_list)
        return pd.DataFrame(matrix, index=self.rownames, columns=self.colnames)

    def gen_dichotomous_preference_matrix(self):
        """Generate dichotomous preference matrix

        Returns:
            dataframe of dichotomous preference matrix
        """
        d_pref_list = [agent.dichotomous_prefrence for agent in self.agents]
        return self.gen_matrix(d_pref_list)

    def gen_ordered_preference_matrix(self):
        """Generate ordered preference matrix

        Returns:
            dataframe of ordered preference matrix
        """
        o_pref_list = [agent.ordered_preference for agent in self.agents]
        return self.gen_matrix(o_pref_list)
