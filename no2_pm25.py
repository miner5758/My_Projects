import pandas as pd
air_quality_no2 = pd.read_csv(r'C:\Users\paula\Downloads\air_quality_no2_long.csv',parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]
#print(air_quality_no2.head())

air_quality_pm25 = pd.read_csv(r'C:\Users\paula\Downloads\air_quality_pm25_long.csv',parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]
#print(air_quality_pm25.head())

air_quality = pd.concat([air_quality_pm25,air_quality_no2],axis=0)
#print(air_quality.head())
#print('Shape of the ``air_quality_pm25`` table: ', air_quality_pm25.shape)
#print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)
#print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)

air_quality = air_quality.sort_values('date.utc')
#print(air_quality.head())

Air_quality = pd.concat([air_quality_pm25,air_quality_no2], keys=["PM25", "NO2"])
#print(air_quality.head())

stations_coord = pd.read_csv(r'C:\Users\paula\Downloads\air_quality_stations.csv')
#print(stations_coord.head())
#print(air_quality.head())

Air_Quality = pd.merge(air_quality,stations_coord, how='left',on='location') ## Using the merge() function, for each of the rows in the air_quality table, the corresponding coordinates are added from the air_quality_stations_coord table. Both tables have the column location in common which is used as a key to combine the information. By choosing the left join, only the locations available in the air_quality (left) table, i.e. FR04014, BETR801 and London Westminster, end up in the resulting table. The merge function supports multiple join options similar to database-style operations.
#print(Air_Quality.head())

air_quality_parameters = pd.read_csv(r"C:\Users\paula\Downloads\air_quality_parameters.csv")
#print(air_quality_parameters.head())

air_quality_p = pd.merge(air_quality,air_quality_parameters, how='left',left_on='parameter',right_on='id') ##Compared to the previous example, there is no common column name. However, the parameter column in the air_quality table and the id column in the air_quality_parameters_name both provide the measured variable in a common format. The left_on and right_on arguments are used here (instead of just on) to make the link between the two tables.
#print(air_quality_p.head())