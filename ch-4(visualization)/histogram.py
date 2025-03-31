import os 
import pandas as pd
import matplotlib.pyplot as plt
directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
pkl_path = os.path.join(directory_path,'avoplotto.pkl')
avocados = pd.read_pickle(pkl_path)
print(avocados.columns)
print(len(avocados))
print(avocados.shape)
avocados['date'] = pd.to_datetime(avocados['date'])

avocados['year'] = avocados['date'].dt.year
print(avocados.columns)
avocados_2016 = avocados[avocados['year']== 2016]
print(avocados_2016.shape)

avocados['year'].plot(kind = 'hist', bins = 5)
plt.show()