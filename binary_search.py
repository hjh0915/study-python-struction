def cul_binary_search(x: int):
    """利用二分查找平方根"""

    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = x 
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        print('low=' + str(low) + 'high=' + str(high) + 'ans=' + str(ans))
        numGuesses += 1
        if ans**2 < x:
            low = ans 
        else:
            high = ans 
        ans = (high + low) / 2.0
    print('numGuesses=' + str(numGuesses))
    print(str(ans) + '平方是' + str(x))

if __name__ == '__main__':
    x = 25
    print(cul_binary_search(x))