def itsTriangularNumber(x):
    tri = x
    for i in range(0, x, 1):
        tri = tri + i
    return tri

def nmbrOfDivisors(x):
    nmbr = 0
    for i in range(1, x+1, 1):
        if x % i == 0:
            nmbr = nmbr + 1
    return nmbr
i = 0
while True:
    i = i + 1
    if nmbrOfDivisors(itsTriangularNumber(i)) >= 500:
        print("Triangular Number: {} , Number of Divisors: {}".format(itsTriangularNumber(i), nmbrOfDivisors(itsTriangularNumber(i))))