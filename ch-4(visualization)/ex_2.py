import os 
import pandas as pd
import matplotlib.pyplot as plt
directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
pkl_path = os.path.join(directory_path,'avoplotto.pkl')
avocados = pd.read_pickle(pkl_path)

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x= 'nb_sold', y= 'avg_price', kind = 'scatter', title = 'Number of avocados sold vs. average price')

# Show the plot
plt.show()