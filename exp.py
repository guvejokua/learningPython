def exp(x, y):
    i = 0
    numberStr = str(x**y)
    for j in range(len(numberStr)):
        i = int(numberStr[j]) + i
    return i

print(exp(2, 1000))