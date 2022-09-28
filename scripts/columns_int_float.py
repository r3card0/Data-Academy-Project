# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from read_dataframe import read_dataframe

def description():
    program_description = """
    This program returns the numerical colums list
    from a dataframe """
    return program_description

df = read_dataframe()

def df_types():
    datatypes = df.convert_dtypes().dtypes
    return datatypes

def numerical_columns():
    columns_int_float = df.dtypes[(df.dtypes == "int64") | (df.dtypes == "float64")] 
    return columns_int_float

def run():
    print(numerical_columns())


if __name__ == "__main__":
    run()