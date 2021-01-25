def selectionSort(alist):
    """选择排序"""
    
    for fillslot in range(len(alist)-1, 0, -1):
        print(alist)

        positionOfMax = 0 
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
            
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp 

    return alist

if __name__ == '__main__':
    x = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(selectionSort(x))