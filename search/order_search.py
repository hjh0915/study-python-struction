def sequentialSearch(alist, item):
    """无序列表的顺序搜索"""
    pos = 0 
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True 
        else:
            pos = pos + 1

    return found

def orderdSequentialSearch(alist, item):
    """有序列表的顺序搜索"""
    pos = 0 
    found = False 
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1 

    return found

if __name__ == '__main__':
    x = [1, 9, 2, 4, 8]
    print(sequentialSearch(x, 4))

    y = [1, 2, 3, 4, 5]
    print(orderdSequentialSearch(y, 8))