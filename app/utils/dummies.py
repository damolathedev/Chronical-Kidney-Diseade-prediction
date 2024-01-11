import pandas as pd

import numpy as np
# import os


# script_dir = os.path.dirname(os.path.realpath(__file__))

# # Specify the relative path to the CSV file in the same folder
# df_csv_path = os.path.join(script_dir, 'dataset.csv')
# data_csv_path = os.path.join(script_dir, "df.csv")

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(df_csv_path)
# df = df.drop("classification", axis=1)
# data = pd.read_csv(data_csv_path, index_col=0)




def dummies(df, data):
    categorical_cols = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
    dummy_df = pd.concat([df, data], ignore_index=True, sort=False)
    array = np.array(pd.get_dummies(dummy_df, columns=categorical_cols).astype(int))
    return array[0]

