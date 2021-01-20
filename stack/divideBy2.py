from basic.demo_stack import Stack 

def divideBy2(decNumber):
    """十进制转二进制"""

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2 
        remstack.push(rem)
        decNumber = decNumber // 2 

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

def baseConverter(decNumber, base):
    """十进制转为任意进制数"""

    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base 
        remstack.push(rem) 
        decNumber = decNumber // base 

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

if __name__ == '__main__':
    x = 233
    base = 8
    print(divideBy2(x))
    print(baseConverter(x, base))
