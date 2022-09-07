def ArraySumOdd(vals):
    response = 0
    for i in vals:
        if i % 2 == 1:
            response = response + i
    return response

def MatrixProductLargerThan(matrixA, val):
    response = 1
    for i in matrixA:
        for j in i:
            if j > val:
                response = response * j
    return response

def polyval(x, coeffs):
    power = 0
    response = 0
    for i in coeffs:
        response = response + (i * (x ** power))
        power = power + 1
    return response

def location_of_largest(matrixA):
    largest = 0
    row = 0
    col = 0
    for i in matrixA:
        for j in i:
            if abs(j) > abs(largest):
                largest = j
                col = i.index(j)
                row = matrixA.index(i)
    return row, col

def main():
    # define the variables needed to test the required functions
    myvals = [-1, 5, 2, -3, 5, 5, 3, -5, 2, 5, 3, 3, 1, 5]
    mymatrix1 = [[1, 3.7, -7, 4], [-8, 9, 2, -1.8], [-12, 7.9, 3.2, 13]]
    mymatrix2 = [[1, 3.7, -7], [-8, 9, -1.8], [7.9, 3.2, -11], [4.3, -0.32, 4]]

    p1 = [3, 1, -2, -4]
    p2 = [2, 1.4, 1, -1, 2]

    x1 = 1.3
    x2 = -2.4

    # for part a)
    ans1 = ArraySumOdd(myvals)
    ans2 = ArraySumOdd(p1)
    print("part a)  ", ans1, ans2)
    print()  # print a blank line

    # for part b)
    ans1 = MatrixProductLargerThan(mymatrix1, x1)
    ans2 = MatrixProductLargerThan(mymatrix2, -1.5)
    print("part b)  ", ans1, ans2)
    print()  # print a blank line

    # for part c)
    poly = polyval(x1, p1)
    print('part c)  Polynomial value for (x1= {:.2f}) = {:.1f}'.format(x1, poly))
    poly = polyval(x2, p2)
    print('part c)  Polynomial value for (x2= {:.2f}) = {:.1f}'.format(x2, poly))
    print()  # print a blank line

    # for part d)
    row, col = location_of_largest(mymatrix1)
    val = mymatrix1[row][col]
    print('part d) ',val,row,col  )
    row, col = location_of_largest(mymatrix2)
    val = mymatrix2[row][col]
    print('part d) ',val,row,col  )

main()
