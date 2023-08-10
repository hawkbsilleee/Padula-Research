import pandas as pd
import matplotlib.pyplot as plt 

#add csv file to dataframe
df = pd.read_csv('dataset2.csv')

#create boxplot
boxplot = df.boxplot(figsize = (5,5), rot = 90, fontsize= '8', grid = False)

plt.title('Control Group')

plt.show()