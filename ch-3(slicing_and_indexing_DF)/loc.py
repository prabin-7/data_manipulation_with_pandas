import os 
import pandas as pd

directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
csv_path = os.path.join(directory_path,'temperatures.csv')
temperatures = pd.read_csv(csv_path,index_col = 0)
print(temperatures.head())

temperatures_srt = temperatures.sort_values('date')

# Subset rows from India, Hyderabad to Iraq, Baghdad


print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad'),'date':'avg_temp_c'])