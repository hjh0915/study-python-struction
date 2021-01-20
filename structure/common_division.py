def calc_common (a:int, b:int) -> int:
    """
        求两个正整数的最大公约数,将两个整数求余a%b=x,
        如果x=0，则b为最大公约数
        如果x!=0,则a=b,b=x
    """
    x = a % b
    while (x != 0):
        a = b
        b = x
        x = a % b

    return b

if __name__ == "__main__":
    print(calc_common(12, 6))
