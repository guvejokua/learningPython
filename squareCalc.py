def delta(a, b, c):
    return b**2 - 4 * a * c


def calc(a, b, c):
    root1 = (b**2 + delta(a, b, c)**0.5)/(2*a)
    root2 = (b ** 2 - delta(a, b, c) ** 0.5) / (2 * a)
    return root1, root2


print("Enter the equation cofficients: a, b, c")
a = int(input())
b = int(input())
c = int(input())

if delta(a, b, c) >= 0:
    root1, root2 = calc(a, b, c)
    print("The equation roots by: {} and {}".format(root1, root2))
else:
    print("The equation haven't real roots")

