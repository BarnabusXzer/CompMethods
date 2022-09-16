def GaussJacobi(A, b, xguess, maxiter=10):

    for i in range(maxiter): # MAXIMUM ITERATIONS

        newGuess = []
        row = 0

        for j in A: # FOR EVERY EQUATION IN THE MATRIX

            col = 0
            equation = [b[row]]
            guess = []
            x = 0

            for k in range(len(j)): # FOR EVERY COEFF IN THE EQUATION
                if col != row:
                    equation.append(-1 * j[k]) # MOVING COEFFS TO THE OTHER SIDE OF THE EQATION                 
                    guess.append(xguess[col]) # CREATING A NEW LIST TO MAKE THE NEXT STEP EASIER
                if k == 0:
                    x = x + equation[k]
                else: 
                    x = x + equation[k] * guess[k-1]
                col = col + 1
            x = x / A[row][row]

            newGuess.append(x)
            row = row + 1
        xguess = newGuess
    return xguess

def main():

    A = [[4,-1,-1],[-2,-3,1],[-1,1,7]]
    b = [3,9,-6]
    xguess = []
    for i in range(len(A)): # FILLS IN xguess WITH ZEROS BASED ON MATRIX SIZE
        xguess.append(0)
    maxiter = 22

    solution = GaussJacobi(A, b, xguess, maxiter) 
    for i in range(len(A)):
        print('x' + str(i) + ' = ' + str(solution[i]))

    print()
    
    A = [[4,3,1,-1],[2,-5,0,-2],[-3,3,-6,1],[0,1,4,8]]
    b = [2,-3,5,-2]
    xguess = []
    for i in range(len(A)): # FILLS IN xguess WITH ONES BASED ON MATRIX SIZE
        xguess.append(1)
    maxiter = 3
    
    solution = GaussJacobi(A, b, xguess, maxiter) 
    for i in range(len(A)):
        print('x' + str(i) + ' = ' + str(solution[i]))

main()