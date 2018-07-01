def t(x):
    xStr = str(x)
    i = 0
    result = 0
    for i in range(0, len(xStr), 1):
        result = result + int(xStr[i])
    return result


def coordinatX(x, y):
    result = 2 * t(x * y)
    return result


def coordinatY(z):
    result = t(z)
    return result


def isPrime(x):
    i = 0
    for i in range(2, x, 1):
        if x % i == 0:
            return False
    return True


def isLess(x, y):
    if x > y:
        return True
    else:
        return False


def control1(x):
    xStr = str(x)
    i = 0
    for i in range(0, len(xStr), 1):
        if int(xStr[i]) == 0:
            return False
        if int(xStr[i]) == 7:
            return False
        if int(xStr[i]) == 8:
            return False
        if int(xStr[i]) == 9:
            return False

    return True


def control2(x):
    xStr = str(x)
    i = 0
    j = 1
    for i in range(0, len(xStr) - 1, 1):
        for j in range(i + 1, len(xStr), 1):
            if int(xStr[i]) == int(xStr[j]):
                return False
    else:
        return True


def control3(x):  # Sıralama kontrolü-------------
    xStr = str(x)
    i = 0
    lesserThan = int(xStr[0])
    for i in range(1, len(xStr), 1):
        if int(xStr[i]) <= lesserThan:
            return False
        lesserThan = int(xStr[1])
    return True


def control4(x, y):
    xStr = str(x)
    yStr = str(y)
    i = 0
    j = 0
    if x - y <= 99:
        return False
    for i in range(0, len(xStr), 1):
        for j in range(0, len(xStr), 1):
            if int(xStr[i]) == int(yStr[j]):
                return False
    return True


def find(x, y):
    i = 0
    if isLess(x, y):
        i = i + 1
        # print("{} > {}".format(x,y))
    else:
        return 11
    if isPrime(x):
        # print("{} is primex".format(x))
        i = i + 1
    else:
        return 12
    if isPrime(y):
        # print("{} is primey".format(y))
        i = i + 1
    else:
        return 13
    if control1(x):
        i = i + 1
        # print("{} control1x".format(x))
    else:
        return 14
    if control1(y):
        i = i + 1
        # print("{} control1y".format(y))
    else:
        return 15
    if control2(x):
        i = i + 1
        # print("{} control2x".format(x))
    else:
        return 16
    if control2(y):
        i = i + 1
        # print("{} control2y".format(y))
    else:
        return 17
    if control3(x - y):
        i = i + 1
        # print("{} control3x".format(x))
    else:
        return 18
    if control4(x, y):
        i = i + 1
    else:
        return 19
    return i


i = 0
j = 0
result = 0
for i in range(100, 999, 1):
    for j in range(100, 999, 1):
        result = find(i, j)
        if result == 9:
            print(i, j, result)
            print(coordinatX(i, j))
            print(coordinatY(9041))
