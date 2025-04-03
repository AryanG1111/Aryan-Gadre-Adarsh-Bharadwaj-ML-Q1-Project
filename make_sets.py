import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv('heart_full.csv')

print(df.columns)
df1 = df[['ST', 'angina', 'chest', 'oldpeak', 'sex', 'hr', 'target']]
df2 = df[['age', 'sex', 'chest', 'cholesterol', 'hr', 'angina', 'oldpeak', 'ST', 'target']]
df3 = df[['chest', 'ST', 'ecg', 'bs', 'sex', 'cholesterol', 'target']]
df4 = df[['ST', 'angina', 'chest', 'oldpeak', 'sex', 'hr', 'cholesterol', 'target']]
df5 = df[['ecg', 'age', 'bps', 'cholesterol', 'hr', 'target']]

df1train, df1test = train_test_split(df1, test_size=0.15)
df1train.to_csv('df1train.csv', index=False)
df1test.to_csv('df1test.csv', index=False)

df2train, df2test = train_test_split(df2, test_size=0.15)
df2train.to_csv('df2train.csv', index=False)
df2test.to_csv('df2test.csv', index=False)

df3train, df3test = train_test_split(df3, test_size=0.15)
df3train.to_csv('df3train.csv', index=False)
df3test.to_csv('df3test.csv', index=False)

df4train, df4test = train_test_split(df4, test_size=0.15)
df4train.to_csv('df4train.csv', index=False)
df4test.to_csv('df4test.csv', index=False)

df5train, df5test = train_test_split(df5, test_size=0.15)
df5train.to_csv('df5rain.csv', index=False)
df5test.to_csv('df5test.csv', index=False)