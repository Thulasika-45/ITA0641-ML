import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

data = pd.read_csv(r"C:\Users\Madhu\Documents\machine learning\CarPrice.csv")

selected_features = ["symboling", "wheelbase", "carlength", "carwidth", "carheight",
                     "curbweight", "enginesize", "boreratio", "stroke", "compressionratio",
                     "horsepower", "peakrpm", "citympg", "highwaympg"]

X = data[selected_features].values
y = data["price"].values

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor()
model.fit(xtrain, ytrain)

r2_score = model.score(xtest, ytest)
print("R-squared Score:", r2_score)

predictions = model.predict(xtest)
mae = mean_absolute_error(ytest, predictions)
print("Mean Absolute Error:", mae)
