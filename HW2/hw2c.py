def GaussJacobi(A, b, xguess, maxiter=10):

    response = 0   


 
    return response

def main():

    A = [[4,-1,-1],[-2,-3,1],[-1,1,7]]
    b = [3,9,-6]
    xguess = [0,0,0]
    maxiter = 22
    print(GaussJacobi(A, b, xguess, maxiter))
    
    A = [[4,3,1,-1],[2,-5,0,-2],[-3,3,-6,1],[0,1,4,8]]
    b = [2,-3,5,-2]
    xguess = [1,1,1,1]
    print(GaussJacobi(A, b, xguess, maxiter))

main()