import functions

def Secant(func, x0, x1, maxiter=15, xtol=0.0001):

    x = 0
    step = (x1 - x0) / maxiter
    xi = x0
    xf = x0 + step

    for i in range(maxiter):
        x = xf- ((xi - xf)/(func(xi) - func(xf))) * func(xf)
        xi = xf
        xf = x
        if abs(xi - xf) < xtol:
            return x
    
    return x

def main():

    func = functions.Function1
    x0 = 1
    x1 = 2
    maxiter = 5
    xtol = 0.0001
    print(Secant(func, x0, x1, maxiter, xtol))

    func = functions.Function2
    x0 = 1
    x1 = 2
    maxiter = 15
    xtol = 0.00000001
    print(Secant(func, x0, x1, maxiter, xtol))

    func = functions.Function2
    x0 = 1
    x1 = 2
    maxiter = 3
    xtol = 0.00000001
    print(Secant(func, x0, x1, maxiter, xtol))

main()