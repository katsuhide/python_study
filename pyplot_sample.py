# グラフ化に必要なものの準備
import matplotlib
import matplotlib.pyplot as plt

# データの扱いに必要なライブラリ
import pandas as pd
import numpy as np
import datetime as dt

plt.style.use('ggplot')
font = {'family' : 'meiryo'}
matplotlib.rc('font', **font)

url = 'https://vincentarelbundock.github.io/Rdatasets/csv/robustbase/ambientNOxCH.csv'
df_sample = pd.read_csv(url, parse_dates=1, index_col=1)

# dfの準備
df = df_sample.iloc[:, 1:]

# df_monthlyの準備
df_monthly = df.copy()
df_monthly.index = df_monthly.index.map(lambda x: x.month)
df_monthly = df_monthly.groupby(level=0).sum()

df_monthly.plot.bar(y=['ad', 'ba', 'se'], alpha=0.6, figsize=(12,3))
plt.title(u'普通の棒グラフ', size=16)
plt.show()
