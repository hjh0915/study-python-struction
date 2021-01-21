from basic.deque import Deque

def palchecker(aString):
    """回文检测"""

    chardeque = Deque()
    
    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True 

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False 
    
    return stillEqual

if __name__ == '__main__':
    x = "asfsefs"
    print(palchecker(x))
    y = "radar"
    print(palchecker(y))