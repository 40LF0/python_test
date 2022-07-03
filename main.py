import numpy as np
from test import *

def update_dic_1(params):
	parameters = params.copy()
	parameters["1"] = parameters["1"] + 100
	parameters["2"] = parameters["2"] + 200
	return parameters

def update_dic_2(params):
	parameters = params.copy()
	parameters["1"] += 100
	parameters["2"] += 200
	return parameters

def main():
    test(update_dic_1)
    test(update_dic_2)

if __name__ == "__main__":
	main()
