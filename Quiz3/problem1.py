from numpy.linalg import solve

def main():
    A = [(4,-2.5,3,1),
        (1,3.5,-4,0),
        (3,1,2,2),
        (2,4,1,5)]

    b = [(1),
        (-7),
        (5),
        (2)]
    solutions = solve(A,b)
    for i in range(len(solutions)):
        print(f'Variable {i} = {solutions[i]:.3f}')

main()
