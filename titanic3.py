import pandas as pd

titanic = pd.read_csv(r'C:\Users\paula\Downloads\titanic.csv')
#print(titanic.head())

air_quality = pd.read_csv(r'C:\Users\paula\Downloads\air_quality_long.csv',index_col='date.utc', parse_dates=True) ##The usage of the index_col and parse_dates parameters of the read_csv function to define the first (0th) column as index of the resulting DataFrame and convert the dates in the column to Timestamp objects, respectively.
#print(air_quality.head())
#print(titanic.sort_values(by='Age').head())
#print(titanic.sort_values(by=['Pclass','Age'],ascending=False).head())

no2 = air_quality[air_quality['parameter'] == 'no2']
no2_subset = no2.sort_index().groupby('location').head(2)
#print(no2_subset)

#print(no2_subset.pivot(columns='location',values='value'))
#print(no2.head())
#no2.pivot(columns='location',values='value').plot()
#print(air_quality.pivot_table(values='value',index='location',columns='parameter',aggfunc='mean')) ##In the case of pivot(), the data is only rearranged. When multiple values need to be aggregated (in this specific case, the values on different time steps) pivot_table() can be used, providing an aggregation function (e.g. mean) on how to combine these values.
#print(air_quality.pivot_table(values='value',index='location',columns='parameter',aggfunc='mean',margins=True))

no2_pivoted = no2.pivot(columns='location',values='value').reset_index()
#print(no2_pivoted.head())

no_2 = no2_pivoted.melt(id_vars='date.utc')
#print(no_2.head())

No_2 = no2_pivoted.melt(id_vars='date.utc',value_vars=["BETR801", "FR04014", "London Westminster"],value_name='NO_2',var_name='Id_location') ## value_vars defines explicitly which columns to melt together. var_name provides a custom column name for the column collecting the column header names. Otherwise it takes the index name or a default variable
##value_name provides a custom column name for the values column instead of the default column name value. Hence, the arguments value_name and var_name are just user-defined names for the two generated columns. The columns to melt are defined by id_vars and value_vars.

#print(No_2.head())