import numpy as np
import pandas as pd
from numpy.linalg import inv
from io import StringIO
from requests import get


url = "https://raw.githubusercontent.com/plotly/datasets/master/mtcars.csv"
s = get(url).content
cars = pd.read_csv(StringIO(s.decode('utf-8')))
    
def my_reg(formula, data):
    
    formula = formula.replace(" ", "")
    y, predictors = formula.split("~")
    predictors = predictors.split("+")
    onevec = np.ones(len(data))
    X = pd.DataFrame(onevec)
    X[predictors] = data[predictors]
    y = np.array(data[y])
    y.shape = (len(data), 1)
    XtX = inv(X.T.dot(X))
    XtXt = XtX.dot(X.T)
    return XtXt.dot(y)

coefs1 = my_reg('mpg ~ cyl', cars)
coefs1

coefs2 = my_reg('mpg ~ cyl + disp', cars)
coefs2

coefs3 = my_reg('mpg ~ cyl + hp', cars)
coefs3
