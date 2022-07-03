import numpy as np
from test_utils import single_test

def test(target):
  parameters = {"1" : np.array([1,2,3]) , "2" : np.array([4,5,6])}
  test_case = {"input" :[parameters]}
  single_test(test_case,target)
