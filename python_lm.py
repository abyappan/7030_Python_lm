#!/usr/bin/env python

# # Python Linear Modeling Assignment
# BSGP 7030 - 2023

# Import pandas, sklearn, matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


# Set notebook variables 
filename = 'regrex1.csv'


# use read_csv() to read regex.csv file
dataset = pd.read_csv(filename)
dataset.describe()
dataset


# Fitting linear regression to the dataset
model = LinearRegression()
model.fit(dataset[['x']], dataset[['y']])


# Visualizing the Linear Regresion Results

# Scatter plot of original dataset
plt.scatter(dataset[['x']], dataset[['y']], color = 'red')
plt.title('y vs x')
plt.title('Raw y vs x')
plt.xlabel('x')
plt.ylabel('y')


# Linear model of dataset
plt.plot(dataset[['x']], model.predict(dataset[['x']]), color = 'blue')
plt.title('y vs x')
plt.title('Linear Model of y vs x')
plt.xlabel('x')
plt.ylabel('y')


# Combined plot
plt.scatter(dataset[['x']], dataset[['y']], color = 'red')
plt.plot(dataset[['x']], model.predict(dataset[['x']]), color = 'blue')
plt.title('y vs x')
plt.xlabel('x')
plt.ylabel('y')
