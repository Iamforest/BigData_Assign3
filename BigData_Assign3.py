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

def allNullEbola(x):
    total = 0
    for i in x:
        total += i 
    return total


print("This is allNullEbola: ", '\n', allNullEbola(num_missing), '\n')




print("this is ebola.isnull", '\n', ebola.isnull(), '\n')

print("this is counting ebola.isnull", '\n', np.count_nonzero(ebola.isnull()), '\n')

ebola_dropped_na = ebola.dropna()
print("this is ebola.fillna", '\n', ebola.fillna(0), '\n')
print("this is ebola_dropped_na", '\n', ebola_dropped_na, '\n')



df7 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(df7)

def my_SQR(x):
    return x * x;

df8 = df7["a"].apply(my_SQR)
print(df8)

df9 = df7.apply(my_SQR)
print(df9)

ebola2 = ebola.fillna(3555)
print(ebola2)

