import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

# df = pd.DataFrame(np.random.randn(10, 3),
#                   columns=['Col1', 'Col2', 'Col3'])
# df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A',
#                      'B', 'B', 'B', 'B', 'B'])
# boxplot = df.boxplot(by='X')

df = pd.read_csv('main_dataset.csv')

df.transpose()

series_list = []
for _ in range(22):
    series_list.append('Experimental')
for _ in range(22, len(df)):
    series_list.append('Control')
df['Group'] = pd.Series(series_list)

# print(df)
boxplot = df.boxplot(by='Group')
plt.show()



