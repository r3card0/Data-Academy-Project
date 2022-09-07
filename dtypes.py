# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from read_dataframe import read_dataframe

def description():
    program_description = """
    This program returns datatypes from each
    column from the dataframe  """
    return program_description

df = read_dataframe()

def df_types():
    datatypes = df.convert_dtypes().dtypes
    return datatypes

def run():
    print(df_types())


if __name__ == "__main__":
    run()