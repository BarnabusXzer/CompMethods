def SumTermProductNotEqual(array1, array2):

    response = 0
    for i in range(len(array1)):
        x = array1[i]
        y = array2[i] 
        if x == y:
            pass
        else:
            response = response + x * y
    return response

def main():
    array1 = [1,7,7,8,2,5,9,3]
    array2 = [2,4,7,7,-2,5,-6,5]
    print(SumTermProductNotEqual(array1, array2))

    array1 = [2,7,7]
    array2 = [2,2,7]
    print(SumTermProductNotEqual(array1, array2))

main()