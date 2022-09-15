def GaussJacobi(A, b, xguess, maxiter=10):

    response = []
    guess = xguess

    for i in range(maxiter): # MAXIMUM ITERATIONS
        for j in A: # FOR EVERY EQUATION IN THE MATRIX
            print(j)
            equation = None #XXX
            count = 0
            for k in j:
                print(k)
        exit        

    return response

def main():

    A = [[4,-1,-1],[-2,-3,1],[-1,1,7]]
    b = [3,9,-6]
    # USING numpy.zeros WOULD SIMPLIFY CREATING THE INITIAL QUESS ARRAY
    xguess = []
    for i in range(len(A)):
        xguess.append(0)
    maxiter = 22
    print(GaussJacobi(A, b, xguess, maxiter))
    
    A = [[4,3,1,-1],[2,-5,0,-2],[-3,3,-6,1],[0,1,4,8]]
    b = [2,-3,5,-2]
    # USING numpy.zeros WOULD SIMPLIFY CREATING THE INITIAL QUESS ARRAY
    xguess = []
    for i in range(len(A)):
        xguess.append(1)
    maxiter = 3
    # print(GaussJacobi(A, b, xguess, maxiter))

main()