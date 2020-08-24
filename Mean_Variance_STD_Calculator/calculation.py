import numpy as np

def calculate(list1):
  if len(list1) < 9:
    raise ValueError('List must contain  9 numbers')
  if not type(list1) is list:
    raise TypeError('Please pass list of values to calculate function')
  else:
    b = np.reshape(list1,(3,3))

  calculations = {
    'mean': [(np.mean(b,axis=0)).tolist(),(np.mean(b,axis=1)).tolist(),(np.mean(b)).tolist()],
    'variance': [(np.var(b,axis=0)).tolist(),(np.var(b,axis=1)).tolist(),(np.var(b)).tolist()],
    'standard deviation': [(np.std(b,axis=0)).tolist(),(np.std(b,axis=1)).tolist(),(np.std(b)).tolist()],
    'min': [(np.min(b,axis=0)).tolist(),(np.min(b,axis=1)).tolist(),(np.min(b)).tolist()],
    'max': [(np.max(b,axis=0)).tolist(),(np.max(b,axis=1)).tolist(),(np.max(b)).tolist()],
    'sum': [(np.sum(b,axis=0)).tolist(),(np.sum(b,axis=1)).tolist(),(np.sum(b)).tolist()]
    }
  return calculations
