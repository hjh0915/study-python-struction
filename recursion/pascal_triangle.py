def generate(numRows: int):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    upper = generate(numRows - 1)
    upper.append([1] + [upper[-1][i-1] + upper[-1][i] for i in range(1, numRows-1)] + [1])
    return upper
    
if __name__ == '__main__':
    print(generate(5))