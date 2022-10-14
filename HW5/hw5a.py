from scipy.optimize import fsolve

def solveSystem():

    ma = 50
    mb = 15

    def function(variables):
        (T,aa,ab) = variables
        eq2 = aa + (3 * ab)
        eq3 = (3 * T) - (mb * 9.81) - (mb * -1 * ab)
        eq4 = T - (ma * 9.81) - (50 * -1 * aa)
        return [eq2,eq3,eq4]

    result = fsolve(function, (0,0,0))
    return(result)

def main():
    result = solveSystem()
    print(f'aa = {result[2]:.3f}\nab = {result[1]:.3f}\nT = {result[0]:.3f}')

main()
