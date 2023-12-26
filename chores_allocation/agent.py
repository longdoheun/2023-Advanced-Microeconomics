"""
Module providing class Agent
"""

import random
import numpy as np


class Agent:
    """Class of agent object with preferences
        (i) dichotomous preferences
        (ii) ordered preferences

    Args:
        n_time_slot: the number of time slots; int
        agents: the list of class 'Agent'; list[Agent]

    Attributes:
        name: the name of agent; str
        n_time_slot: the number of time slots; int
        ordered_preference : assigned ordered preference or randomly generated ordered preference; dataframe
        dichotomous_preference : dichotomous preference based on ordered_preference; dataframe
    """

    def __init__(self, name, n_time_slot):
        self.name = name
        self.n_time_slot = n_time_slot
        self.ordered_preference = self.gen_ordered_preference()
        self.dichotomous_prefrence = self.gen_dichotomous_prefernence()

    def gen_ordered_preference(self):
        """Generate random ordered preference based on the number of time slots

        Returns:
            randomly generated ordered preferences; dataframe
        """
        n_available_time = random.randint(2, self.n_time_slot)
        preference = np.concatenate(
            (
                np.arange(1, n_available_time + 1),
                np.zeros(self.n_time_slot - n_available_time, dtype=int),
            )
        )
        np.random.shuffle(preference)
        return preference

    def gen_dichotomous_prefernence(self):
        """Generate dichotomous preferences based on the ordered preference

        Returns:
            dichotomous preferences; dataframe
        """
        dichotomous_prefernence = self.ordered_preference.copy()
        dichotomous_prefernence[dichotomous_prefernence != 0] = 1
        return dichotomous_prefernence
