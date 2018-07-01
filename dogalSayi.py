def kareleriToplami(x):
    result = 0
    for i in range(0, x+1, 1):
        result = result + i**2
    return result

def toplamlariKaresi(x):
    result = 0
    for i in range(0, x+1, 1):
        result = result + i
    result = result**2
    return result

print(toplamlariKaresi(10)-kareleriToplami(10))