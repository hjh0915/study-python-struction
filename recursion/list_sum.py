def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i 

    return theSum

def listsum_by_recursion(numList):
    """使用递归求和"""
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum_by_recursion(numList[1:])

if __name__ == '__main__':
    x = [1, 3, 5, 7, 9]
    print(listsum(x))
    print(listsum_by_recursion(x))