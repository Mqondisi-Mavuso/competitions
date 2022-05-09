import math

strCases = input()
cases = int(strCases)
pi = math.pi


def getSum(totalSum, r):
    global pi
    theSum = round(totalSum + (pi * (r*r)), 6)
    return theSum


def getR2(r, a):
    if int(r * a) > 0:
        return int(r * a)
    else:
        return 0


def getR3(r, b):
    if int(r / b) > 0:
        return int(r / b)
    else:
        return 0


def printOutput():
    global totalSum
    global case
    print(f"Case #{case}: {totalSum}")


case = 0

while cases:
    totalSum = 0
    myList = list(map(int, input().split()))
    case += 1
    r1 = myList[0]
    a = myList[1]
    b = myList[2]

    if r1 > 0:
        totalSum = getSum(totalSum, r1)
    else:
        printOutput()
    r = r1
    while r:
        r2 = getR2(r1, a)
        if r2:
            totalSum = getSum(totalSum, r2)
            
        else:
            printOutput()
            break

        r3 = getR3(r2, b)
        if r3:
            totalSum = getSum(totalSum, r3)
        else:
            printOutput()
            break
        r1 = int(r3)
        r = r1 * r2 * r3

    cases -= 1
