import numpy as np
import matplotlib.pyplot as plt

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
        print("2" + str(func(xi)) + str(func(xf)))
        print(xi, xf)
        print(abs(xi - xf))
        print(x)
        if abs(xi - xf) < xtol:  
            return x        
 
    return x

def Time(wspec):
    va = 115
    kt = .366
    ra = 2.11
    irotor = 0.0133
    c = 0.002792

    wss = (kt * va) / ((kt ** 2) + (ra * c))
    cv = (kt * va) / (ra * irotor)
    cw = ((c * ra) + (kt ** 2)) / (ra * irotor)

    if type(wspec) == int or type(wspec) == float:
        if wspec > (0.999999 * wss):
            return -1
    else:
        if any(wspec) > (0.999999 * wss):
            return -1

    def func(x):
        return (1 / (cv - cw))

    time = (Simpson(func, 0, wspec))
    return time

def Speed(tspec):
    
    def func(x):
        return (Time(x) - tspec)

    speed = Secant(func, 275, 325)
    return speed

def main():

    va = 115
    kt = .366
    ra = 2.11
    c = 0.002792
    wss = (kt * va) / ((kt ** 2) + (ra * c))

    print(f'The Steady-State Motor Speed is{wss: .2f} radians/second')

    wspec = 280
    print(f'The Motor Needs{Time(wspec): .3f} seconds To Reach{wspec: .0f} radians/second')

    tspec = 0.35
    # print(f'The Motor Will Reach{Speed(tspec): .2f} radians/second at{tspec: .2f} seconds')

    x = np.linspace(.000001,300)
    y = Time(x)
    plt.plot(x,y)
    plt.xlim(0,300)
    plt.xlabel('Speed - radians/second')
    plt.ylim(0,0.3)
    plt.ylabel('Time - seconds')
    plt.show()

main()