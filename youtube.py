import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\paula\Downloads\CAvideos.csv",index_col='title')
top_5 = data.head(6)
print(top_5)

fig,axs = plt.subplots(figsize=(19,6))
likes = top_5['likes']
#likes.plot.bar(ax=axs)

dislikes = top_5['dislikes']
#dislikes.plot.bar(ax=axs)

views = top_5['views']
#views.plot.bar(ax=axs)