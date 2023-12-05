import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('./data/salaries.csv', sep=',')

X = df[['years_experience']]
y = df['salary']

model = LinearRegression()
model.fit(X.values, y.values)

predictions = model.predict([[14], [12]])
print(predictions)


