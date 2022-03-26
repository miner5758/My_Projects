import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv(r"air_quality_no2.csv",index_col=0, parse_dates=True) ##The usage of the index_col and parse_dates parameters of the read_csv function to define the first (0th) column as index of the resulting DataFrame and convert the dates in the column to Timestamp objects, respectively.
print(air_quality.head())
#air_quality.plot()
#air_quality['station_paris'].plot()
#air_quality.plot.scatter(x='station_london', y='station_paris', alpha=0.5)
#air_quality.plot.box()
#axs = air_quality.plot.area(figsize=(12,4), subplots=True)

fig,axs = plt.subplots(figsize=(12,4)) # Create an empty matplotlib Figure and Axes
air_quality.plot.area(ax=axs) # Use pandas to put the area plot on the prepared Figure/Axes
axs.set_ylabel('NO$_2$ concentration') # Do any matplotlib customization you like
#fig.savefig('no2_concentrations.png') # Save the Figure/Axes using the existing matplotlib method.
