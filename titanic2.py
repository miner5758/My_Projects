import pandas as pd

titanic = pd.read_csv(r'C:\Users\paula\Downloads\titanic.csv')
#print(titanic.head())
#print(titanic['Age'].mean())
#print(titanic[['Age','Fare']].median())
#print(titanic[['Age','Fare']].describe())

#print(titanic.agg( 
 #   {
  #   'Age': ['min', 'max', 'median', 'skew'],
    # 'Fare': ['min', 'max', 'median', 'mean']
    # }
   # )
   # )
#print(titanic[['Sex','Age']].groupby('Sex').mean())
#print(titanic.groupby('Sex').mean())
#print(titanic.groupby('Sex')['Age'].mean()) #It does not make much sense to get the average value of the Pclass. if we are only interested in the average age for each gender, the selection of columns (rectangular brackets [] as usual) is supported on the grouped data as well:
#print(titanic.groupby(['Sex','Pclass'])['Fare'].mean())
#print(titanic['Pclass'].value_counts())
print(titanic.groupby('Pclass')['Pclass'].count())