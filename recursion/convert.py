# import sys 
# sys.path.append("..") 
# from basic.stack import Stack

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

def toStr2(n, base):
    rStack = Stack()
    convertString = "0123456789ABCDEF"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStr2(n//base, base)

if __name__ == '__main__':
    print(toStr(10, 2))
    print(toStr(10, 8))
    print(toStr(10, 16))