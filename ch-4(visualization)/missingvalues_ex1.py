# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import os 
import pandas as pd
directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
pkl_path = os.path.join(directory_path,'avoplotto.pkl')
avocados_2016 = pd.read_pickle(pkl_path)
# print(avocados.columns)
# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind= 'bar')

# Show plot
plt.show()