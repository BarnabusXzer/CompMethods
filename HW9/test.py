from scipy.optimize import minimize
import pandas as pd
import numpy as np

data = pd.read_csv('Data_File_1.txt', sep='\t', lineterminator='\n')
data.rename(columns = {'Y\r':'Y'}, inplace = True)
xdata = data['X'].values
ydata = data['Y'].values

def func(coeffs,x):
    data = coeffs[0] + coeffs[1] * np.exp(coeffs[2] * x)
    error = 0
    for i in range(len(data)):
        error = error + abs(data[i] - ydata[i])
        print(error)
    return error

res = minimize(func,[1,1,1],args=(xdata),method='Nelder-Mead')
print(f'A = {res.x[0]}\nB = {res.x[1]}\nC ={res.x[2]}')