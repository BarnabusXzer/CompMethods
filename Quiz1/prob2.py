
def MatrixColumnSum(matrix,colnum):
    
    responseNum = 0
    responseString = ''
    count = 0

    for i in matrix: 
        responseNum = responseNum + i[colnum]
        if count == 0:
            responseString = responseString + str(i[colnum])
        else:
            responseString = responseString + ' + ' + str(i[colnum])
        count = count + 1
        if count == len(matrix):
            responseString = responseString + ' = ' + str(responseNum)

    return responseNum, responseString

def main():

    matrix = [[1,2.5,3,6],[3,5,2.1,3],[4,3.7,2,5.1]]
    colnum = 2
    response = MatrixColumnSum(matrix,colnum)
    print(str(response[0]) + '\n' + response[1])

    matrix = [[1,2.5],[3,5],[2.1,3],[4,3.7],[2,5.1]]
    colnum = 0
    response = MatrixColumnSum(matrix,colnum)
    print(str(response[0]) + '\n' + response[1])

main()