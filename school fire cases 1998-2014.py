import pandas as pd

df = pd.read_csv("school_fire_cases_1998_2014.csv")

print(df)

#Total Population
print(df['Population'].sum())

#find the lesser or greater year of population
print(df.loc[df['Year'] < 1999, ['Population', 'Year']])

#How many cases are held over a year & population
print(df.loc[df['Cases'] >0, ['Population', 'Year']])

#find the top 5 largest population w.r.t year
print(df.nlargest(5, 'Population'))

#find the top 5 smallest population w.r.t year
print(df.nsmallest(5, 'Population'))

