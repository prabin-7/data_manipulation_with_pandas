# Subset for Egypt to India
import os 
import pandas as pd

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
csv_path = os.path.join(parent_path,'temperatures.csv')

temperatures = pd.read_csv(csv_path, index_col = 0)
print(temperatures.columns)
temperatures['date'] = pd.to_datetime(temperatures['date'])
temperatures['year'] = temperatures['date'].dt.year

temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index = ['country', 'city'], columns= 'year')

temp_by_country_city_vs_year.loc['Egypt':'India']

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')])

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),2005:2010]