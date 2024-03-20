import pandas as pd

df = pd.read_csv("simplified_municipality_indicators.csv")

print(df)

#sort by the reported crime values
print(df.sort_values(by='reportedCrime'))

#filter of cars & motorcycle column
print(df.filter(items=['cars', 'motorcycles']))

#drop the satisfactionInfluence column
df1 = df.drop(columns=['satisfactionInfluence'], axis=1)
print(df1)

#drop the 2nd & 4th row
df2 = df.drop([1, 3], axis=0)
print(df2)

#sort the ascending order of medianIncome column
print(df.sort_values('medianIncome', ascending=True))


#find how many null values in satisfactionGeneral column
print(df['satisfactionGeneral'].isnull().sum())

#print the all column names
print(df.columns.values)

