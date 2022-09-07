import functions

def Simpson(func, a, b, npoints = 35):

    if not (npoints % 2 == 1):
        npoints = npoints + 1

    response = 0
    h = (b - a)/npoints
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

def main():
    
    func = functions.Function1
    a = 1
    b = 3
    npoints = 10
    print(Simpson(func, a, b, npoints))

    func = functions.Function2
    a = 2
    b = 3 
    npoints = 23
    print(Simpson(func, a, b, npoints))

    func = functions.Function3
    a = 2
    b = 3
    print(Simpson(func, a, b))

main()