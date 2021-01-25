def shellSort(alist):
    """希尔排序（跳跃间隔两两比较排序）"""

    # 增量（sublistcount）为多少，就有多少个子列表
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("增量为", sublistcount, "这个列表为", alist)

        sublistcount = sublistcount // 2
    
    return alist
    
def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap 

        alist[position] = currentvalue

if __name__ == '__main__':
    x = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(shellSort(x))