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

def Time(wspec):
    va = 115
    kt = .366
    ra = 2.11
    irotor = 0.0133
    c = 0.002792

    wss = (kt * va) / ((kt ** 2) + (ra * c))
    cv = (kt * va) / (ra * irotor)
    cw = ((c * ra) + (kt ** 2)) / (ra * irotor)

    def func(x):
        return (1 / (cv - cw))

    time = Simpson(func, 0, wspec)
    
    if time > (0.999999 * wss):
        return -1
    else: 
        return time, wss

def Speed(tspec):
    
    def func(x):
        return (Time(x)[0] - tspec)

    speed = Secant(func, -2, 350)
    return speed

def main():
    
    print(f'The Steady-State Motor Speed is {Time(0)[1]: .2f} radians/second')

    wspec = 280
    print(f'The Motor Needs{Time(wspec)[0]: .3f} seconds To Reach{wspec: .0f} radians/second')

    tspec = 0.35
    print(f'The Motor Will Reach {Speed(tspec): .2f} radians/second at {tspec: .2f} seconds')

main()