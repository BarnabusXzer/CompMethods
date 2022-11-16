from scipy.optimize import minimize
import pandas as pd
import numpy as np

data = pd.read_csv('Data_File_1.txt', sep='\t', lineterminator='\n')
data.rename(columns = {'Y\r':'Y'}, inplace = True)
x = data['X'].values
y = data['Y'].values

def func(x,a,b,c):
    return a + b * np.e ** (c * x)

res = minimize(func,x)
