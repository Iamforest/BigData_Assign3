#Author: Michael Forest McDonald
#Assignment 3
#03/02/2023

import pandas as pd
import matplotlib.pyplot as plt

plt.ion()

#read the data file and store it as a data frame
df = pd.read_csv("F:\CSU\BigData_Assign3_repo\gapminder.tsv", sep = '\t')

# exploration commmands
print(df.head(5),'\n', 
      type(df),'\n', 
      df.shape,'\n', 
      df.columns,'\n', 
      df.dtypes,'\n')

# Creating more dataframes from the main dataframe
df1 = df['country']
print(df1.head(5), '\n')

df2 = df[['country', 'lifeExp', 'gdpPercap']]
print(df2.head(5), '\n')

# Slicing
df_rows = df.loc[35:40]
print(df_rows.head(5), '\n')


# NoSQL grouping
print(df.groupby("country")["lifeExp"].mean(), '\n')

print(df.groupby("country")["gdpPercap"].mean().mean(),'\n')

print(df.groupby("year")["lifeExp"].mean(), '\n')

print(df.groupby("continent")["lifeExp", "gdpPercap"].mean(), '\n')

print(df.nunique(), '\n')

print(df.value_counts(), '\n')

# Plotting

df3 = df.groupby("year")["lifeExp"].mean()

df3.plot()





