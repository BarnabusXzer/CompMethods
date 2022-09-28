import math

def Simpson(func, a, b, npoints = 99):

    if not (npoints % 2 == 1):
        npoints = npoints + 1

    response = 0
    h = (b - a) / npoints
    for i in range(npoints + 1):
        x = a + h * i
        if (i == 0):
            response = func(x)
        elif (i % 2 == 0):
            response = response + (2 * func(x))
        else:
            response = response + (4 * func(x))
    response = (h / 3) * response

    return response

def Secant(func, x0, x1, maxiter=99, xtol=0.0001):

    x = 0
    xi = x0
    xf = x0 + ((x1 - x0) / maxiter)

    for i in range(maxiter):
        x = xf - ((xi - xf) / (func(xi) - func(xf))) * func(xf)
        xi = xf
        xf = x
        if abs(xi - xf) < xtol:  
            return x        
    
    return x

def SigmaMax(z):

    length = 320

    def func(x):
        return x * (1.5 * math.cos(x / length)) 

    mroot = Simpson(func, 0, length)
    sigmamax = mroot / z
    return sigmamax

def DesignTheSpar(DesignStress):
    
    def func(x):
        return SigmaMax(x) - DesignStress

    z = Secant(func, .001, 10)
    return z

def main():
    z = 3.5
    print(f'Wing Section Modulus:{z: .1f}\nWing-Stress:{SigmaMax(z): .1f}\n')

    z = 1.5
    print(f'Wing Section Modulus:{z: .1f}\nWing-Stress:{SigmaMax(z): .1f}\n')

    DesignStress = 25000
    print(f'Design-Stress:{DesignStress: .2f}\nWing Section Modulus:{DesignTheSpar(DesignStress): .2f}\n')

main()