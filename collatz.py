def odd(n):
    return 3*n + 1


def even(n):
    return n/2


def sequence(n):
    count = 0
    newN = 0
    if n % 2 == 0:
        newN = even(n)
        count = count + 1
    else:
        newN = odd(n)
        count = count + 1

    print(newN)
    if newN != 1:
        sequence(newN)
    if newN == 1:
        return newN
        print("r")


print(sequence(13))