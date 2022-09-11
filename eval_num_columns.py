# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from read_dataframe import read_dataframe
from identify_NaN_values import null_values
from columns_int_float import numerical_columns

def description():
    program_description = """
    This program creates a list of new variables
    with the purpose to clean dataframe
    """
    return program_description

df = read_dataframe()
columns_int_float = numerical_columns()
isnull_eval_list = []
var_list = []
new_var_list = []
var = "column"

#create a list of expressions
def create_expressions():
    for i,j in columns_int_float.items():
        isnull_eval_list.append(f"df['{i}].isnull().values.any()")
    
    return isnull_eval_list

expression_list = create_expressions()

#create a list of variables 
def create_variables():
    for c in range(len(expression_list)):
        var_list.append(var + str(c+1) + " = " )
    
    return var_list

variables_list = create_variables()

#assign expressions to variables.
def create_new_variables():
    for variable in range(len(variables_list)):
        for expression in range(len(expression_list)):
            if variable == expression:
                new_var_list.append((variables_list[variable]+expression_list[expression]))
    
    return new_var_list

new_var_list = create_new_variables()
#List new variables
def list_new_variables():
    for e in new_var_list:
        print(e)

def run():
    print(description())
    print(list_new_variables())


if __name__ == "__main__":
    run()

