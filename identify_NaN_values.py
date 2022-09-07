# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from read_dataframe import read_dataframe

df = read_dataframe()

def identify_nan():
    value_null = df.isnull().values.any()
    return value_null

def run():
    print(identify_nan())


if __name__ == "__main__":
    run()