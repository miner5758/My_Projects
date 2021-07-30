import pandas as pd

titanic = pd.read_csv(r"C:\Users\paula\Downloads\titanic.csv")
#print(titanic.head())

ages = titanic['Age'] ##Each column in a DataFrame is a Series. As a single column is selected, the returned object is a pandas Series. We can verify this by checking the type of the output:
#print(type(titanic['Age'])) 
#print(ages.head())
#print(titanic["Age"].shape) ##DataFrame.shape is an attribute (remember tutorial on reading and writing, do not use parentheses for attributes) of a pandas Series and DataFrame containing the number of rows and columns: (nrows, ncolumns). A pandas Series is 1-dimensional and only the number of rows is returned.

age_sex = titanic[['Age','Sex']] ##To select multiple columns, use a list of column names within the selection brackets [].
#print(age_sex.head())
#print(type(titanic[['Age','Sex']]))
#print(titanic[['Age','Sex']].shape)


above_35 = titanic[titanic['Age'] > 35] ##The condition inside the selection brackets titanic["Age"] > 35 checks for which rows the Age column has a value larger than 35:
#print(above_35.head())
#print(titanic['Age'] > 35) ##returns true or false
#print(above_35.shape)

Class_23 = titanic[titanic['Pclass'].isin([2,3])] ##Similar to the conditional expression, the isin() conditional function returns a True for each row the values are in the provided list. To filter the rows based on such a function, use the conditional function inside the selection brackets []. In this case, the condition inside the selection brackets titanic["Pclass"].isin([2, 3]) checks for which rows the Pclass column is either 2 or 3.
#print(Class_23.head())
class_32 = titanic[(titanic['Pclass'] == 3) | (titanic['Pclass'] == 2)]
#print(class_32.head())

age_no_na = titanic[titanic['Age'].notna()] ##The notna() conditional function returns a True for each row the values are not an Null value. As such, this can be combined with the selection brackets [] to filter the data table.
#print(age_no_na.head())
#print(age_no_na.shape)

adult_names = titanic.loc[titanic['Age'] > 35, 'Name'] ##In this case, a subset of both rows and columns is made in one go and just using selection brackets [] is not sufficient anymore. The loc/iloc operators are required in front of the selection brackets []. When using loc/iloc, the part before the comma is the rows you want, and the part after the comma is the columns you want to select.
#print(adult_names.head())

#print(titanic.iloc[9:25, 2:5])

titanic.iloc[0:3, 3] = "anonymous" ##When selecting specific rows and/or columns with loc or iloc, new values can be assigned to the selected data. For example, to assign the name anonymous to the first 3 elements of the third column:
#print(titanic['Name'].head)