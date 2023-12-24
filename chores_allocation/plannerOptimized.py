from .preferenceMatrix import PreferenceMatrix
import numpy as np
import pandas as pd

def LeastDemadedSlot(dichotomous_submatrix: pd.DataFrame):
  column_wise = np.sum(dichotomous_submatrix, axis=0)
  least_demanded_slots = np.where(column_wise == np.min(column_wise))[0]
  return least_demanded_slots

def MaximumLeastDemandedSlot(ordered_submatrix: pd.DataFrame, least_demanded_slots: np.ndarray):
  max_value = np.max(ordered_submatrix.iloc[:,least_demanded_slots])
  maximum_least_demanded_slots = np.where(ordered_submatrix.iloc[:,least_demanded_slots] == max_value)

  rand = np.random.randint(0, len(maximum_least_demanded_slots[1]))
  
  psi_mld = maximum_least_demanded_slots[0][rand] # row-wise selection
  phi_mld = maximum_least_demanded_slots[1][rand]
  
  rowname = ordered_submatrix.iloc[:,least_demanded_slots].index[psi_mld]
  colname = ordered_submatrix.iloc[:,least_demanded_slots].columns[phi_mld]

  return rowname, colname

def planner_optimized_algorithm(P:PreferenceMatrix):
  allocation_matrix = P.zeros.copy()
  sub_d_matrix = P.dichotomous.copy()
  sub_o_matrix = P.ordered.copy()
  iteration = 0

  while True:
    iteration += 1
    least_demanded_slots = LeastDemadedSlot(sub_d_matrix)

    print(least_demanded_slots)

    if len(least_demanded_slots) != 0:
      rowname, colname = MaximumLeastDemandedSlot(sub_d_matrix, least_demanded_slots)

      allocation_matrix.loc[rowname, colname] = 1
      sub_d_matrix = sub_d_matrix.drop(index = rowname, columns= colname)
      sub_o_matrix = sub_o_matrix.drop(index = rowname, columns= colname)

      print("Round", iteration)
      print(allocation_matrix)
      print(sub_o_matrix)

    else:
      return allocation_matrix