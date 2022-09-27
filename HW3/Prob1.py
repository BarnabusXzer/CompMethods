import math
from urllib import response

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

def Secant(func, x0, x1, maxiter=49, xtol=0.0001):

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

def STO(thrust):
    w = 56000
    s = 1000
    clmax = 2.4
    cd = 0.0279
    rho = 0.002377
    gc = 32.2

    vstall = math.sqrt((w) / (.5 * rho * s * clmax))
    vto = 1.2 * vstall
    A = gc * (thrust / w)
    B = (gc / w) * (.5 * rho * s * cd)

    def func(x):
        return (x / (A - (B * (x ** 2))))

    sto = Simpson(func, 0, vto)
    return sto

def ThrustNeededForTakeoff(distance):
    w = 56000
    s = 1000
    clmax = 2.4
    cd = 0.0279
    rho = 0.002377
    gc = 32.2

    def func(x):
        return STO(x) - distance

    root = Secant(func, 950, 1550)
    return root

        
def main():

    thrust = 13000
    print(f'Required Takeoff Distance With {thrust} Pounds of Thrust: {STO(thrust): .1f} Feet')

    distance = 1500
    print(f'The Required Thrust To Takeoff In {distance} Feet: {ThrustNeededForTakeoff(distance): .2f} Pounds')

    distance = 1000
    print(f'The Required Thrust To Takeoff In {distance} Feet: {ThrustNeededForTakeoff(distance): .2f} Pounds')

main()