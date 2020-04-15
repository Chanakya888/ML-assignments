
#CREATE RANDOM DATA FOR MULTIPLE LINEAR REGRESSION

import numpy as np
import pandas as pd
import scipy
import random
from scipy.stats import norm
random.seed(1)
n= 3
X=[]
for i in range(0,n):
    X_i= scipy.stats.norm.rvs(0, 1, 100)
    X.append(X_i)
eps=scipy.stats.norm.rvs(0, 1, 100)
y = 1 + (0.5 * X[0]) + (0.4 * X[1]) + (0.3 * X[2])  + eps
data_ols = {'X0': X[0],'X1':X[1],'X2':X[2] ,'Y': y }
df = pd.DataFrame(data_ols)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

#CREATE RANDOM DATA FOR LOGISTIC REGRESSION

X = []
n = 3
for i in range(0,n):
  X_i = scipy.stats.norm.rvs(0, 1, 100)
  X.append(X_i)
odds = (np.exp(1 + (0.5 * X[0]) + (0.4 * X[1]) + (0.3 * X[2])) /(1 + np.exp(1 + (0.5 * X[0]) + (0.4 * X[1]) + (0.3 * X[2]) )))
y1 = [ ]
for i in odds:
  if (i>=0.5):
    y1.append(1)
  else:
    y1.append(0)
data_lr = {'X0': X[0],'X1':X[1],'X2':X[2] ,'Y': y1 }
df1 = pd.DataFrame(data_lr)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

#CREATE RANDOM DATA FOR k-MEANS CLUSTERING

X_a= -2 * np.random.rand(100,2)
X_b = 1 + 2 * np.random.rand(50,2)
X_a[50:100, :] = X_b
plt.scatter(X_a[ : , 0], X_a[ :, 1], s = 50)
plt.show()
data_kmeans = {'X0': X_a[:,0],'X1':X_a[:,1]}
df3 = pd.DataFrame(data_kmeans)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())