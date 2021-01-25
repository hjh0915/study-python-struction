def bubbleSort(alist):
    """冒泡排序"""
    
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                # print(alist)
                # temp为临时存储的位置
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def shortBubbleSort(alist):
    """短冒泡排序"""

    exchanges = True 
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False 
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1
    return alist

if __name__ == '__main__':
    x = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(bubbleSort(x))
    print(shortBubbleSort(x))