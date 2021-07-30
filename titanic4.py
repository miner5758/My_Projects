import pandas as pd

titanic = pd.read_csv(r"C:\Users\paula\Downloads\titanic.csv")
#print(titanic.head())

#print(titanic['Name'].str.lower())
#print(titanic['Name'].str.split(','))

titanic['Surname'] = titanic['Name'].str.split(',').str.get(0) #Using the Series.str.split() method, each of the values is returned as a list of 2 elements. The first element is the part before the comma and the second element is the part after the comma. As we are only interested in the first part representing the surname (element 0), we can again use the str accessor and apply Series.str.get() to extract the relevant part. Indeed, these string functions can be concatenated to combine multiple functions at once! 
#print(titanic['Surname'])
#print(titanic[titanic['Name'].str.contains('Countess')]) #The string method Series.str.contains() checks for each of the values in the column Name if the string contains the word Countess and returns for each of the values True (Countess is part of the name) or False (Countess is not part of the name). This output can be used to subselect the data using conditional (boolean) indexing introduced in the subsetting of data tutorial. As there was only one countess on the Titanic, we get one row as a result.
#print(titanic['Name'].str.len())
#print(titanic['Name'].str.len().idxmax())
#print(titanic.loc[titanic['Name'].str.len().idxmax(),'Name'])

titanic['Sex_short'] = titanic['Sex'].replace({'male':'M','female':'F'})
print(titanic['Sex_short'])