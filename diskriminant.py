def control1(pswStr):
    if int(pswStr[5]) == 1:
        return True
    elif int(pswStr[5]) == 3:
        return True
    elif int(pswStr[5]) == 5:
        return True
    elif int(pswStr[5]) == 7:
        return True
    else:
        return False


def control2(pswStr):
    if int(pswStr[5]) % 2 == 0:
        return False
    else:
        return True


def control3(pswStr):
    if int(pswStr[1]) + int(pswStr[5]) == 8:
        return True
    else:
        return False

def control5(psw):
    i = 0
    for i in range(2, psw - 1, 1):
        if psw % i == 0:
            return False
    else:
        return True

def control4(pswStr):
    i = 0
    j = 1
    for i in range(0, len(pswStr)-1, 1):
        for j in range(i+1, len(pswStr), 1):
            if int(pswStr[i]) == int(pswStr[j]):
                return False
    else:
        return True

def control6(pswStr):
    if int(pswStr[:2]) + int(pswStr[2:]) == 2018:
        return True
    else:
        return False

def passWord(psw):
    say = 0
    pswStr = str(psw)
    if control1(pswStr):
        say = say + 1
    else:
        return 0
    if control2(pswStr):
        say = say + 1
    else:
        return 0
    if control3(pswStr):
        say = say + 1
    else:
        return 0
    if control4(pswStr):
        say = say + 1
    else:
        return 0
    if control5(psw):
        say = say + 1
    else:
        return 0
    if control6(pswStr):
        say = say + 1


    return say


a = 0
for a in range(700000, 999999, 1):
    strA = str(a)
    if int(strA[5]) % 2 == 1:
        if passWord(a) == 6:
            print("True : {}".format(a))
