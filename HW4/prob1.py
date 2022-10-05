from scipy.integrate import quad
from math import cos, sin, pi
import numpy as np
import matplotlib.pyplot as plt

def FourierCoeffs(func, L, nterms):

    a = np.zeros(nterms)
    b = np.zeros(nterms)

    def an_func(x):
        return (func(x) * cos((pi * x * i) / L))

    def bn_func(x):
        return (func(x) * sin((pi * x * i) / L))

    for i in range(nterms):
        a[i] = (1 / L) * quad(an_func, -L, L)[0]
        b[i] = (1 / L) * quad(bn_func, -L, L)[0]

    return a, b

def PlotFourier(func, L, nterms, xmin, xmax, npoints=5000):
    
    a, b = FourierCoeffs(func, L, nterms)

    x = np.linspace(xmin, xmax, npoints)
    y = np.zeros_like(x)

    def f(z):
        return (a[i] * cos((pi * z * i) / L)) + (b[i] * sin((pi * z * i) / L))
    sudof = np.vectorize(f)

    for i in range(len(a)):
        y = y + sudof(x)

    plt.plot(x,y,L)
    plt.show()

def main(): 
 
    def Sharkfin(x): 
        if x < 0: return (x + 1) ** 3 
        else: return 1 - x ** 3 
     
    def Squarewave(x): 
        if x < 0: return 1 
        else: return -1 
 
    L = 1 
    a, b = FourierCoeffs(Sharkfin, L, 50) 
    print(a, "\n",b,"\n") 
    PlotFourier(Sharkfin, L, 50, -3*L, 3*L) 
 
    L = 0.75 
    a, b = FourierCoeffs(Squarewave, L, 50) 
    print(a, "\n",b,"\n") 
    PlotFourier(Squarewave, L, 50, -3*L, 3*L) 
 
    L = np.pi 
    a, b = FourierCoeffs(lambda x: -x, L, 10) 
    print(a, "\n",b,"\n") 
    PlotFourier(lambda x: -x, L, 10, -4*L, 4*L, npoints=10000) 
 
main() 
