def alpToVal(s):
    if s == 'A' or s == 'a':
        return 0
    if s == 'B' or s == 'b':
        return 1
    if s == 'C' or s == 'c':
        return 2
    if s == 'Ç' or s == 'ç':
        return 3
    if s == 'D' or s == 'd':
        return 4
    if s == 'E' or s == 'e':
        return 5
    if s == 'F' or s == 'f':
        return 6
    if s == 'G' or s == 'g':
        return 7
    if s == 'Ğ' or s == 'ğ':
        return 8
    if s == 'H' or s == 'h':
        return 9
    if s == 'I' or s == 'ı':
        return 10
    if s == 'İ' or s == 'i':
        return 11
    if s == 'J' or s == 'j':
        return 12
    if s == 'K' or s == 'k':
        return 13
    if s == 'L' or s == 'l':
        return 14
    if s == 'M' or s == 'm':
        return 15
    if s == 'N' or s == 'n':
        return 16
    if s == 'O' or s == 'o':
        return 17
    if s == 'Ö' or s == 'ö':
        return 18
    if s == 'P' or s == 'p':
        return 19
    if s == 'R' or s == 'r':
        return 20
    if s == 'S' or s == 's':
        return 21
    if s == 'Ş' or s == 'ş':
        return 22
    if s == 'T' or s == 't':
        return 23
    if s == 'U' or s == 'u':
        return 24
    if s == 'Ü' or s == 'ü':
        return 25
    if s == 'V' or s == 'v':
        return 26
    if s == 'Y' or s == 'y':
        return 27
    if s == 'Z' or s == 'z':
        return 28

def stringtoValue(st):
    i = 0
    value = 0
    for i in range(0, len(st), 1):
        if i % 2 == 0:
            value = value + alpToVal(st[i])
        else:
            value = value - alpToVal(st[i])
    return value

print(stringtoValue("kasiyopeya"))