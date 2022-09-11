# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from read_dataframe import read_dataframe
from identify_NaN_values import null_values
from dtypes import df_types

def description():
    program_description = """
    This program creates a list of new variables
    with the purpose to clean dataframe
    """
    return program_description

df = read_dataframe()
columns_int_float = df_types()
isnull_eval_list = []
var_list = []
good_list = []
var = "column"

#create expressions
def cr_expressions():
    for i,j in columns_int_float.items():
        isnull_eval_list.append(f"df['{i}].isnull().values.any()")
    
    return isnull_eval_list

def run():
    print(cr_expressions())


if __name__ == "__main__":
    run()

