import numpy as np
import matplotlib.pyplot as plt
 
# FUNCTION TO FIND DETERMINATE OF A MATRIX
def determinant(Matrix):
    n = len(Matrix)
    AM = np.copy(Matrix)
    for fd in range(n):
        for i in range(fd+1,n):
            if AM[fd][fd] == 0:
                AM[fd][fd] == 1.0e-18
            crScaler = AM[i][fd] / AM[fd][fd] 
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
    product = 1.0
    for i in range(n):
        product *= AM[i][i] 
 
    return product

def LeastSquares(x,y,power):

    x = x
    y = y

    coeffs = []

    N = len(x)
    M = np.zeros(shape=(power+1,power+1))
    Mi = np.zeros(shape=(power+1,power+1))
    b = np.zeros(shape=(power+1,1))

    # FOR LOOPS TO CREATE MATRIX b
    for i in range(len(b)):
        total = 0
        for j in range(N):
            total = total + ((x[j] ** i) * y[j])
        b[i][0] = total

    # FOR LOOPS TO CREATE MATRIX M
    for i in range(len(M)):
        for j in range(len(M)):
            
            total = 0
            for z in range(N):
                total = total + (x[z] ** (i + j))
            M[i][j] = total

            if i == 0 and j == 0:
                M[i][j] = N

    # FOR LOOPS TO CHANGE ROW i TO MATRIX b
    for i in range(len(Mi)):
        
        # REPLACE CORRECT COLUMN WITH MATRIX b
        Mi = np.copy(M)
        for j in range(len(Mi)):
            Mi[j][i] = b[j][0]

        # FIND DETERMINATE OF M AND Mi THEN FIND COEFFS
        MDeterm = determinant(M)
        MiDeterm = determinant(Mi)
        coeffs.append(MiDeterm / MDeterm)

    return coeffs

def PlotLeastSquares(x,y,power, showpoint=True, npoints=500):
    
    coeffs = LeastSquares(x, y, power)
    rcoeffs = []
    for value in coeffs:
        rcoeffs = [value] + rcoeffs
    xrange = np.linspace(min(x), max(x), npoints)

    def func(x):
        return np.polyval(rcoeffs, x)

    yy = func(xrange)

    plt.plot(xrange,yy)
    if showpoint == True:
        plt.scatter(x,y)
    plt.show()

def main():


    x = [.05,.11,.15,.31,.46,.52,.7,.74,.82,.981,.17]
    y = [.956,1.09,1.332,.717,.771,.539,.378,.370,.306,.242,.104]

    print()
    power = 1
    coeffs = LeastSquares(x,y,power)
    for i in range(len(coeffs)):
        print(f'Coefficient-{i}: {coeffs[i]: .4f}')
    PlotLeastSquares(x,y,power)
    print()

    power = 3
    coeffs = LeastSquares(x,y,power)
    for i in range(len(coeffs)):
        print(f'Coefficient-{i}: {coeffs[i]: .4f}')
    PlotLeastSquares(x,y,power,False)
    print()


    for i in range(0, (len(x) - 5)):
        x.pop()
        y.pop()

    power = 2
    coeffs = LeastSquares(x,y,power)
    for i in range(len(coeffs)):
        print(f'Coefficient-{i}: {coeffs[i]: .4f}')
    PlotLeastSquares(x,y,power)
    print()

main()