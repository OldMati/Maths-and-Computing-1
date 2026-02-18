import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

R = 4
A = math.pi * R ** 2
L = 50

fig, ax = plt.subplots()

with open('Session3/FairGroundData.csv', 'r') as file:
    df = pd.read_csv(file)

#remove 1st row, convert to float
df = df.iloc[1:]
df = df.astype(float, errors='ignore')

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df[df['Force'] > 0]

df['Stress'] = df['Force'] / A
df['Strain 1'] = (df['Strain 1'] / 100)

print(df.head())

#df[['Strain 1', 'Stress']].plot(x='Strain 1', y='Stress', title='Strain vs Stress')
#plt.show()

#df[(df['Stress'] > 25) & (df['Time'] < 109.93)][['Strain 1', 'Stress']].plot(x='Strain 1', y='Stress', title='Strain vs Stress for elastic region')
#plt.show()

idx = df[df['Strain 1'] < 0.001].idxmax()
print(idx)

elasticRegion = df[(df['Stress'] > 25) & (df['Time'] < 109.93)]

dStress = elasticRegion['Stress'].max() - elasticRegion['Stress'].min()
dStrain = elasticRegion['Strain 1'].max() - elasticRegion['Strain 1'].min()

E = dStress / dStrain

print(f'Youngs modulus: {E}')



df['Crosshead Strain'] = df['Extension'] / L

df[df['Crosshead Strain'] > 0.055][['Crosshead Strain', 'Stress']].plot(
    ax=ax,
    x='Crosshead Strain', 
    y='Stress', 
    title='Stress vs Strain')
#plt.show()


fakeElReg = df[(df['Crosshead Strain'] < 0.0733) & (df['Crosshead Strain'] > 0.055)]
fakeElReg[['Crosshead Strain', 'Stress']].plot(x='Crosshead Strain', y='Stress', ax=ax, label='Elastic Modulus', color='tab:orange')
plt.show()


dFakeStress = fakeElReg['Stress'].max() - fakeElReg['Stress'].min()
idx = fakeElReg.idxmax()
dFakeStrain = df.iloc[10993]['Crosshead Strain'] - fakeElReg['Crosshead Strain'].min()

Efake = dFakeStress / dFakeStrain
print('EFAKE: ', Efake)

#FINDING YIEL strength and UTS
minidx = 10993
maxidx = 20000

YS = (df.iloc[minidx:maxidx]['Stress'].min(), df.iloc[df.iloc[minidx:maxidx]['Stress'].idxmin()]['Crosshead Strain'])
UTS = (df['Stress'].max(), df.iloc[df['Stress'].idxmax()]['Crosshead Strain'])
print('Yield Strength, UTS: ', YS, UTS)

