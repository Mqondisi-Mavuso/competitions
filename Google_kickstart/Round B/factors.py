# from functools import reduce
# import math
#
#
# def factors(n):
#     return list(reduce(list.__add__,
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
#
#
# def printOutput():
#     global numPalindrome
#     global case
#     print(f"Case #{case}: {numPalindrome}")
#
#
# def rev(num):
#     return int(num != 0) and ((num % 10) * \
#              (10**int(math.log(num, 10))) + \
#                           rev(num // 10))
#
#
# def isPalindrome(n):
#     if n == rev(n):
#         return True
#     else:
#         return False
#
#
# strCases = input()
# cases = int(strCases)
# numPalindrome = 0
# case = 0
#
# while cases:
#     # getting factors
#     myList = []
#     sNum = input()
#     num = int(sNum)
#     if num < 0:
#         num *= -1
#
#     elif num == 0:
#         numPalindrome = 1
#         printOutput()
#         cases -= 1
#         continue
#
#     myList = factors(num)
#     case += 1
#     # checking for palindrome
#     for n in myList:
#         if isPalindrome(n):
#             numPalindrome += 1
#     printOutput()
#     numPalindrome = 0
#     cases -= 1

def palins():
    n=0
    while True:
        n+=1
        m=(n+1)//2                                      # get the floor value after dividing by two
        for i in range(10**(m-1),10**m):                # 10 ^(m-1)
            if n%2==1:                                  # if there is a remainder after dividing by two
                yield int(str(i)+str(i)[-2::-1])
            else:
                yield int(str(i)+str(i)[::-1])

for case in range(1,int(input())+1):
    p=palins()
    n=int(input())
    m=0
    while True:
        t=next(p)
        if t>n or t>=10**5:break
        if n%t==0:m+=1
    for k in range(1,10**5):
        if n%k==0 and n//k>=10**5 and str(n//k)==str(n//k)[::-1]:m+=1
    print('Case #',case,': ',m,sep='')
