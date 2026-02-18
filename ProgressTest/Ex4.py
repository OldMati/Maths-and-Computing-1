import numpy as np
import pandas as pd


with open('ProgressTest/Data.csv', 'r') as file:
    df = pd.read_csv(file)

#print(df.head())

#df = df.iloc[1:]
df = df.astype(float, errors='ignore')

#print(df.head())

print('max of b:', df['b'].max())

count = 0

for cell in df.iloc[0:]['c']:
    if cell < 60:
        count += 1

print('count: ', count)