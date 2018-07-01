def d(n):
    result = 0
    i = 0
    for i in range(1, n, 1):
        if n % i == 0:
            result = result + i
    return result


def calculate(n):
    bolen = d(n)
    if bolen != n:
        if n == d(bolen):
            return True
    return False


total = 0
i = 0
for i in range(1, 10000, 1):
    if calculate(i):
        print("Bağdaşık sayı : {}".format(i))
        total = total + d(i)
print(total)