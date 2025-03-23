import pandas as pd
import numpy as np
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
print(file_path)
csv_path = os.path.join(file_path,'sales_subset.csv')

df = pd.read_csv(csv_path, index_col = 0)

print(df.head(),'\n',df.shape)