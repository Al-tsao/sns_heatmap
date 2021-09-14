#Standard

import numpy as np

import pandas as pd

from numpy.random import randn

from pandas import Series, DataFrame

#Stats

from scipy import stats

#Matplotlib

import matplotlib as mpl

import matplotlib.pyplot as plt

#Seaborn

import seaborn as sns

#Draw

sns.set() #設定繪圖改為seaborn繪製

df = sns.load_dataset('flights')

df  = df.pivot(index='month',columns='year',values='passengers')

heatmap = sns.heatmap(df, cmap='rocket_r') #cmap:制定熱力圖顏色

heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=30) #繪製x軸標示角度

heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation=0) #繪製y軸標示角度

plt.xlabel('Year')

plt.ylabel('Month')

plt.title('this is a demo')

plt.show() #繪圖