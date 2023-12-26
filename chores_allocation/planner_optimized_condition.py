"""
Module providing chores allocation algorithm under the planner optimized condtion
"""

import numpy as np
import pandas as pd
from .preference_matrix import PreferenceMatrix


def least_demaded_slot(dichotomous_submatrix: pd.DataFrame):
    """Find least demanded slot and row-wise selection.

    Args:
        ordered_submatrix: ordered (sub)matrix; dataframe
        least_demanded_slots: index of LD; NDarray

    Returns:
        dataframe of allocation matrix
    """
    column_wise = np.sum(dichotomous_submatrix, axis=0)
    least_demanded_slots = np.where(column_wise == np.min(column_wise))[0]
    return least_demanded_slots


def maximum_least_demanded_slot(
    ordered_submatrix: pd.DataFrame, least_demanded_slots: np.ndarray
):
    """Find maximum least demanded slot and row-wise selection.
    If MLD is multiple, randomly choose the slot.

    Args:
        ordered_submatrix: ordered (sub)matrix; dataframe
        least_demanded_slots: index of LD; NDarray

    Returns:
        rowname: name of selected row
        colname: name of selected column
    """
    max_value = np.max(ordered_submatrix.iloc[:, least_demanded_slots])
    maximum_least_demanded_slots = np.where(
        ordered_submatrix.iloc[:, least_demanded_slots] == max_value
    )

    rand = np.random.randint(0, len(maximum_least_demanded_slots[1]))

    psi_mld = maximum_least_demanded_slots[0][rand]  # row-wise selection
    phi_mld = maximum_least_demanded_slots[1][rand]

    rowname = ordered_submatrix.iloc[:, least_demanded_slots].index[psi_mld]
    colname = ordered_submatrix.iloc[:, least_demanded_slots].columns[phi_mld]

    return rowname, colname


def planner_optimized_algorithm(preference: PreferenceMatrix):
    """Execute planner optimized chores allocation

    Args:
        preference: instance of class PreferenceMatrix

    Returns:
        dataframe of allocation matrix
    """
    allocation_matrix = preference.zeros.copy()
    sub_d_matrix = preference.dichotomous.copy()
    sub_o_matrix = preference.ordered.copy()
    iteration = 0

    while True:
        iteration += 1
        least_demanded_slots = least_demaded_slot(sub_d_matrix)

        print(least_demanded_slots)

        if len(least_demanded_slots) != 0:
            rowname, colname = maximum_least_demanded_slot(
                sub_d_matrix, least_demanded_slots
            )

            allocation_matrix.loc[rowname, colname] = 1
            sub_d_matrix = sub_d_matrix.drop(index=rowname, columns=colname)
            sub_o_matrix = sub_o_matrix.drop(index=rowname, columns=colname)

            print("Round", iteration)
            print(allocation_matrix)
            print(sub_o_matrix)

        else:
            return allocation_matrix
