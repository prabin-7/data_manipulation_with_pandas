# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import os 
import pandas as pd

directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
pkl_path = os.path.join(directory_path,'avoplotto.pkl')
avocados = pd.read_pickle(pkl_path)
# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind = 'bar', title = 'avocados sold by size')

# Show the plot
plt.show()