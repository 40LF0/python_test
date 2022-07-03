import numpy as np
def single_test(test_case,target):
    target_answer = target(*test_case["input"])
    print(target_answer)
