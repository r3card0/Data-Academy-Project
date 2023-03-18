import pandas as pd
import numpy as np

class FillNaN:
    def __init__(self,dataframe) -> None:
        self.dataframe = dataframe

    def fill_numerical(self):
        self.numerical_column_list = self.dataframe.dtypes[(self.dataframe.dtypes == 'int64') | (self.dataframe.dtypes == 'float64')].index

        for col in self.numerical_column_list:
            self.dataframe[col].replace(np.nan,0,inplace=True)

        return self.dataframe
    

df = pd.read_csv('/Users/ideasleon/platzi_edu/Python/DataAcademy/ProyDataAcademy/Doc/largest_us_retailers.csv')

df_test = FillNaN(df)
print(df_test.fill_numerical())