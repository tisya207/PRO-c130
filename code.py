import pandas as pd 
import csv

df= pd.read_csv("merged_stars_data_final.csv")
print(df.shape)

del df["Luminosity"]

print(df.shape)

df = df.rename({
                'Star_name': "star_names", 
                'Distance': "distance", 
                'Mass': "mass", 
                'Radius': "radius", 
                'Luminosity': "luminosity", 
            }, axis='columns')

df.to_csv('main2.csv') 