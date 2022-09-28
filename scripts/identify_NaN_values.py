# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from read_dataframe import read_dataframe

def description():
    program_description = """
    This program evaluates if a dataframe has NaN values,
    if true, returns all rows with NaN values
    if not, returns a message: Dataframe free of NaN values  """
    return program_description

df = read_dataframe()

def identify_nan():
    value_null = df.isnull().values.any()
    return value_null

#value_null = identify_nan()

def rows_nan():
    rows_value_null = df[df.isnull().any(axis=1)]
    return rows_value_null

def free_nan():
    free_of_null_values = "Dataframe free of NaN values"
    return free_of_null_values

# Variables
value_null = identify_nan()
rows_value_null = rows_nan()
free_of_null_values = free_nan()

def null_values():
    if value_null == True:
        return rows_value_null
    else:
        return free_of_null_values

def run():
    print(description())
    print(null_values())


if __name__ == "__main__":
    run()