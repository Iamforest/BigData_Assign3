#Author: Michael Forest McDonald
#Assignment 3
#03/02/2023
#Assignment 4
#03/02/2023

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

#read the data file and store it as a data frame
df = pd.read_csv("gapminder.tsv", sep = '\t')

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

#######################################################################
#Assignment 4

df4 = pd.read_csv("concat_1.csv")
df5 = pd.read_csv("concat_2.csv")
df6 = pd.read_csv("concat_3.csv")

dfConcat = pd.concat([df4, df5, df6])

print(dfConcat)

dfConcat2 = pd.concat([df4, df5, df6], axis = 1)

print(dfConcat2)

person = pd.read_csv("survey_person.csv")
site = pd.read_csv("survey_site.csv")
survey = pd.read_csv("survey_survey.csv")
visited = pd.read_csv("survey_visited.csv")

merge1 = site.merge(visited, left_on = "name", right_on = "site")

print(merge1)

ebola = pd.read_csv("country_timeseries.csv")

print("This is ebola.count ", '\n', ebola.count(), '\n')

num_rows = ebola.shape[0]

num_missing = num_rows - ebola.count()

print(num_missing)

#def allNullEbola(x):
#    for i in x:
#        
#print("This is allNullEbola: ", '\n', allNullEbola(num_missing), '\n')




print(ebola.isnull())

print(np.count_nonzero(ebola.isnull()))
