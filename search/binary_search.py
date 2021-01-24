def binarySearch(alist, item):
    """有序列表的二分搜索"""
    first = 0 
    last = len(alist) - 1
    found = False 

    while first <= last and not found:
        midpoint = (first + last) // 2 
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1 
            else:
                first = midpoint + 1
    
    return found 

def binarySearch2(alist, item):
    """二分搜索的递归方式"""
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2 
        if alist[midpoint] == item:
            return True 
        else:
            if item < alist[midpoint]:
                return binarySearch2(alist[:midpoint], item)
            else:
                return binarySearch2(alist[midpoint+1:], item)
        
if __name__ == '__main__':
    x = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    print(binarySearch(x, 44))
    print(binarySearch2(x, 54))