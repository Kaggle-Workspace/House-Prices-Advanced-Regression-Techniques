import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data_train = pd.read_csv(
    "/home/kaustav/Desktop/Kaggle-Workspace/House-Prices-Advanced-Regression-Techniques/data/train.csv")
data_test = pd.read_csv(
    "/home/kaustav/Desktop/Kaggle-Workspace/House-Prices-Advanced-Regression-Techniques/data/test.csv")
print(data_train.describe())

X_train = data_train.loc[:, data_train.columns != "SalePrice"]
y_train = data_train["SalePrice"]

X_test = data_test.loc[:, data_test.columns != "SalePrice"]
y_test = data_test["SalePrice"]

