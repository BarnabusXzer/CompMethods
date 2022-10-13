from tkinter import Variable
import numpy as np

def CreatePowerMatrix(x,M):

    Matrix = np.zeros(shape=(M,M))
    var = 0

    for i in range(M):
        var = ((2 * M) - 2) + (i)
        for j in range(M):

            power = (var) - (2 * j)
            total = 0
            for z in x:
                total = total + (z ** power)

            Matrix[i][j] = total
    return Matrix

def main():
    x = [3,1,6.2,9.5,4.1,-11,5,-2]
    m = CreatePowerMatrix(x,5)
    print(m)
    print()
    m = CreatePowerMatrix(x[:4],3)
    print(m)

main()

