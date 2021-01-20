def calc_pi (n: int) -> float:
    """
        n/4 = 1-1/3+1/5-1/7+...
        求在指定n后的近似值
    """
    sum = 0
    for i in range(1, n):
        if (i % 2) == 0:
            sum += -1/(2*i-1)
        else:
            sum += 1/(2*i-1)

    return 4 * sum 

if __name__ == "__main__":
    x = calc_pi(10000000)
    print(x)
