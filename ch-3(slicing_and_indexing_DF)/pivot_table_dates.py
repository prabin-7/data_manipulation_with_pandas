import os 
import pandas as pd

directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
csv_path = os.path.join(directory_path,'temperatures.csv')
temperatures = pd.read_csv(csv_path,index_col = 0)
print(temperatures.head())
# Add a year column to temperatures

temperatures['year'] = pd.to_datetime(temperatures['date']).dt.year       #date_time stored as a string and then can be trained to be a knight
print(temperatures.head())
# Pivot avg_temp_c by country and city vs year
# temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c',index = ['country','city'], columns = 'year', fill_value = 0)

# # See the result
# print(temp_by_country_city_vs_year)