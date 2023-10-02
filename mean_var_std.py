import numpy as np


def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  new_array = np.array(list)
  new_array_3 = new_array.copy()
  new_array_3 = new_array_3.reshape((3, 3))

  col_mean = np.mean(new_array_3, axis=0).tolist()
  row_mean = np.mean(new_array_3, axis=1).tolist()
  flattened_mean = np.mean(new_array).tolist()

  col_var = np.var(new_array_3, axis=0).tolist()
  row_var = np.var(new_array_3, axis=1).tolist()
  flattened_var = np.var(new_array).tolist()

  col_std = np.std(new_array_3, axis=0).tolist()
  row_std = np.std(new_array_3, axis=1).tolist()
  flattened_std = np.std(new_array).tolist()

  col_max = np.max(new_array_3, axis=0).tolist()
  row_max = np.max(new_array_3, axis=1).tolist()
  flattened_max = np.max(new_array).tolist()

  col_min = np.min(new_array_3, axis=0).tolist()
  row_min = np.min(new_array_3, axis=1).tolist()
  flattened_min = np.min(new_array).tolist()

  col_sum = np.sum(new_array_3, axis=0).tolist()
  row_sum = np.sum(new_array_3, axis=1).tolist()
  flattened_sum = np.sum(new_array).tolist()

  calculations = {
      'mean': [col_mean, row_mean, flattened_mean],
      'variance': [col_var, row_var, flattened_var],
      'standard deviation': [col_std, row_std, flattened_std],
      'max': [col_max, row_max, flattened_max],
      'min': [col_min, row_min, flattened_min],
      'sum': [col_sum, row_sum, flattened_sum]
  }

  return calculations
