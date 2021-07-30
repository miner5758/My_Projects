import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv(r"C:\Users\paula\Downloads\air_quality_no2_long.csv")
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
#print(air_quality.head())
#print(air_quality.city.unique())

air_quality['datetime'] = pd.to_datetime(air_quality['datetime'])
#print(air_quality['datetime'])
#print(air_quality["datetime"].min(), air_quality["datetime"].max())
#print(air_quality['datetime'].max() - air_quality['datetime'].min())

air_quality['month'] = air_quality['datetime'].dt.month ##By using Timestamp objects for dates, a lot of time-related properties are provided by pandas. For example the month, but also year, weekofyear, quarter,… All of these properties are accessible by the dt accessor.
#print(air_quality.head())

#print(air_quality.groupby([air_quality['datetime'].dt.weekday, 'location'])['value'].mean())

#fig, axs = plt.subplots(figsize=(12,4))
#air_quality.groupby(air_quality['datetime'].dt.hour)['value'].mean().plot(kind='bar',rot=0,ax=axs)
#plt.xlabel('Hour of the day')
#plt.ylabel('$NO_2 (µg/m^3)$')

no_2 = air_quality.pivot(index='datetime', columns='location', values='value')
#print(no_2.head())
#print(no_2.index.year,no_2.index.weekday)

#no_2['2019-05-20':'2019-05-21'].plot()

monthly_max = no_2.resample('M').max()
#print(monthly_max.head())

print(no_2.resample('D').mean().plot(style='-o',figsize=(10,5)))