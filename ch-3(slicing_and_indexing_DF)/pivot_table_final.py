import pandas as pd
import os 

pfolder= os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
csv_location = os.path.join(pfolder,'temperatures.csv')

df = pd.read_csv(csv_location, index_col = 0)

# print(df.head())
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# print(df['date'].dtype)    #now : datetime64[ns] before it was object

temp_by_country_city_vs_year = df.pivot_table(values='avg_temp_c', index=['country','city'],columns= 'year', aggfunc= ['sum','median','min','max'], margins= False )
#If all values in a column are NaN (missing), pandas will not display the margins row.
print(temp_by_country_city_vs_year.loc[:,'sum':'median'])
print(temp_by_country_city_vs_year.iloc[:,:10])        #it selects the data not the column header like sum or year

