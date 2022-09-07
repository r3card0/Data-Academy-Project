# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def description():
    program_description = """
    This program read a dataframe
    """
    return program_description

def file_path():
    filepath= input('Type file path: ')
    return filepath

def read_dataframe():
    df = pd.read_csv('Doc/largest_us_retailers.csv')
    return df

def run():
    #print(description())
    read_dataframe()


if __name__ == "__main__":
    run()