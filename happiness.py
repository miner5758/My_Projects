import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"world-happiness-report.csv")
d = data[data['year'] >= 2019]

d = d.drop_duplicates(subset=['Country name'],keep='last')
d.index = d['Country name']

e = d.loc[:,['Freedom to make life choices']]
f = e.tail(10)

fig,axs = plt.subplots(figsize=(14,6))
f.plot.barh(ax=axs, color='Red')
